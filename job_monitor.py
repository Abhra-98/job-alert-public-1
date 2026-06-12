import json
import os
import time
import smtplib
import requests
import feedparser
from google import genai
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from jobspy import scrape_jobs
import pandas as pd

from config import (
    RESUME_TEXT,
    JOB_SEARCHES,
    NAUKRI_SEARCHES,
    EMAIL_SENDER,
    EMAIL_RECEIVER,
)

GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]
GEMINI_API_KEY     = os.environ["GEMINI_API_KEY"]
SEEN_JOBS_FILE     = "seen_jobs.json"

def load_seen_jobs() -> set:
    if os.path.exists(SEEN_JOBS_FILE):
        with open(SEEN_JOBS_FILE, "r") as f:
            return set(json.load(f))
    return set()


def save_seen_jobs(seen: set):
    with open(SEEN_JOBS_FILE, "w") as f:
        json.dump(list(seen), f, indent=2)


# ────────────────────────────────────────────────────────
#  2. LINKEDIN & INDEED — via python-jobspy
# ────────────────────────────────────────────────────────

def fetch_linkedin_indeed_jobs() -> pd.DataFrame:
    all_jobs = []

    for search in JOB_SEARCHES:
        try:
            print(f"  🔍 [{search['site'].upper()}] '{search['search_term']}' in {search['location']}")
            jobs = scrape_jobs(
                site_name      = [search["site"]],
                search_term    = search["search_term"],
                location       = search["location"],
                results_wanted = search.get("results_wanted", 20),
                hours_old      = 24,
                country_indeed = "India",
            )
            if jobs is not None and not jobs.empty:
                jobs["_source"] = search["site"].capitalize()
                all_jobs.append(jobs)
                print(f"     ✅ {len(jobs)} jobs found")
            else:
                print(f"     ℹ️  No results")
            time.sleep(3)

        except Exception as e:
            print(f"     ⚠️  Error: {e}")

    return pd.concat(all_jobs, ignore_index=True) if all_jobs else pd.DataFrame()

def fetch_naukri_jobs() -> pd.DataFrame:
    naukri_jobs = []

    for search in NAUKRI_SEARCHES:
        keyword  = search["keyword"]
        location = search.get("location", "india")
        label    = search.get("label", keyword)

        # Build RSS URL
        rss_url = (
            f"https://www.naukri.com/rss/searchresults.php"
            f"?keyword={keyword.replace(' ', '+')}"
            f"&location={location.replace(' ', '+')}"
            f"&noOfResults=20"
            f"&jobAge=1"   # jobs posted in last 1 day
        )

        print(f"  🔍 [NAUKRI RSS] '{keyword}' in '{location}'")
        print(f"     URL: {rss_url}")

        try:
            # feedparser handles RSS parsing automatically
            feed = feedparser.parse(rss_url)

            status = getattr(feed, "status", "unknown")
            print(f"     HTTP Status: {status}")

            entries = feed.get("entries", [])
            print(f"     ✅ {len(entries)} jobs found in RSS feed")

            if not entries:
                print(f"     ℹ️  Feed bozo flag: {feed.get('bozo', False)}")
                print(f"     ℹ️  Feed bozo exception: {feed.get('bozo_exception', 'none')}")

            for entry in entries:
                try:
                    title       = entry.get("title", "Unknown Role")
                    link        = entry.get("link", "")
                    summary     = entry.get("summary", "")
                    published   = entry.get("published", "Recent")

                    # Extract company and location from summary HTML
                    # Naukri RSS summary contains: Company | Location | Experience
                    company  = "Unknown Company"
                    location_val = location

                    # Parse summary text for company/location
                    import re
                    # Remove HTML tags
                    clean_summary = re.sub(r"<[^>]+>", " ", summary).strip()

                    # Naukri RSS summary format:
                    # "Company Name | Location | X-Y years | Salary"
                    parts = [p.strip() for p in clean_summary.split("|")]
                    if len(parts) >= 1:
                        company = parts[0].strip() or "Unknown Company"
                    if len(parts) >= 2:
                        location_val = parts[1].strip() or location

                    description = f"{title} at {company}. Location: {location_val}. {clean_summary}"

                    naukri_jobs.append({
                        "title"       : title,
                        "company"     : company,
                        "location"    : location_val,
                        "job_url"     : link,
                        "description" : description,
                        "date_posted" : published,
                        "_source"     : "Naukri",
                    })

                except Exception as e:
                    print(f"     ⚠️  Could not parse one entry: {e}")

            time.sleep(2)

        except Exception as e:
            print(f"     ❌ RSS fetch error: {e}")

    return pd.DataFrame(naukri_jobs) if naukri_jobs else pd.DataFrame()


# ────────────────────────────────────────────────────────
#  4. AI ANALYSIS — Google Gemini
# ────────────────────────────────────────────────────────

def analyse_job_fit(title: str, company: str, description: str) -> str:
    client = genai.Client(api_key=GEMINI_API_KEY)

    prompt = f"""
You are an expert career coach and resume analyst.

Compare the candidate's resume against the job description below.
Be specific, honest, and concise.

Reply STRICTLY in this exact format — no extra text:

MATCH SCORE: [X/10]

WHY YOU SHOULD APPLY:
- [reason tied to both resume and job]
- [reason 2]
- [reason 3]

GAPS TO ADDRESS:
- [skill or experience missing, or write "None"]

ONE TIP:
[One actionable sentence on tailoring the application]

=========================
JOB TITLE : {title}
COMPANY   : {company}

JOB DESCRIPTION:
{str(description)[:2500]}

CANDIDATE RESUME:
{RESUME_TEXT[:2500]}
"""

    try:
        response = client.models.generate_content(
            model    = "gemini-2.0-flash",
            contents = prompt,
        )
        return response.text.strip()
    except Exception as e:
        return f"AI analysis unavailable: {e}"


# ────────────────────────────────────────────────────────
#  5. EMAIL — HTML notification via Gmail
# ────────────────────────────────────────────────────────

def send_email(jobs_list: list):
    if not jobs_list:
        print("✅ No new jobs — no email sent.")
        return

    now_str = datetime.now().strftime("%d %b %Y, %I:%M %p")

    source_colors = {
        "LinkedIn" : "#0a66c2",
        "Indeed"   : "#003a9b",
        "Naukri"   : "#ff7555",
    }

    job_blocks = ""
    for job in jobs_list:
        source = job.get("_source", "Portal")
        color  = source_colors.get(source, "#555")
        ai     = job.get("ai_analysis", "Not available.").replace("\n", "<br>")

        job_blocks += f"""
        <div style="background:#f9fafc;border-left:5px solid {color};
                    padding:20px;margin-bottom:24px;border-radius:8px;
                    box-shadow:0 2px 6px rgba(0,0,0,0.06);">
          <div style="font-size:11px;font-weight:bold;color:{color};
                      letter-spacing:2px;text-transform:uppercase;margin-bottom:6px;">
            📌 {source}
          </div>
          <h2 style="margin:0 0 5px;color:#111;font-size:18px;">
            {job.get("title", "Unknown Role")}
          </h2>
          <p style="margin:0 0 12px;font-size:14px;color:#444;">
            🏢 <strong>{job.get("company", "N/A")}</strong>
            &nbsp;|&nbsp; 📍 {job.get("location", "N/A")}
            &nbsp;|&nbsp; 🕐 {job.get("date_posted", "Recent")}
          </p>
          <a href="{job.get("job_url", "#")}"
             style="display:inline-block;background:{color};color:#fff;
                    padding:10px 24px;border-radius:5px;text-decoration:none;
                    font-weight:bold;font-size:13px;margin-bottom:14px;">
            ▶ Apply Now
          </a>
          <div style="background:#fff;border:1px solid #dde3ec;border-radius:6px;
                      padding:14px 16px;font-size:13px;color:#333;line-height:1.9;">
            <strong>🤖 Gemini AI — Resume Match Analysis:</strong><br><br>
            {ai}
          </div>
        </div>
        """

    html_body = f"""
    <html><body style="font-family:Arial,sans-serif;max-width:700px;margin:auto;
                       padding:30px;background:#eef1f7;color:#222;">
      <div style="background:linear-gradient(135deg,#1a1a2e,#16213e);
                  color:#fff;padding:24px 30px;border-radius:12px 12px 0 0;">
        <h1 style="margin:0;font-size:22px;">🆕 {len(jobs_list)} New Job Alert(s)</h1>
        <p style="margin:6px 0 0;font-size:12px;opacity:0.65;">
          {now_str} · LinkedIn + Indeed + Naukri · AI by Google Gemini
        </p>
      </div>
      <div style="background:#fff;padding:28px 30px;
                  border-radius:0 0 12px 12px;border:1px solid #dde1eb;">
        {job_blocks}
      </div>
      <p style="font-size:11px;color:#aaa;text-align:center;margin-top:16px;">
        Job Alert Agent · GitHub Actions · 100% Free
      </p>
    </body></html>
    """

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"🆕 {len(jobs_list)} New Job Alert(s) — {now_str}"
    msg["From"]    = EMAIL_SENDER
    msg["To"]      = EMAIL_RECEIVER
    msg.attach(MIMEText(html_body, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, GMAIL_APP_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print(f"📧 Email sent — {len(jobs_list)} job(s) notified.")
    except Exception as e:
        print(f"❌ Email failed: {e}")


# ────────────────────────────────────────────────────────
#  6. MAIN
# ────────────────────────────────────────────────────────

def main():
    print(f"\n{'='*56}")
    print(f"  JOB ALERT AGENT  |  {datetime.now().strftime('%d %b %Y  %H:%M')}")
    print(f"{'='*56}\n")

    seen = load_seen_jobs()
    print(f"📋 Previously seen jobs: {len(seen)}\n")

    print("── STEP 1: LinkedIn & Indeed ─────────────────────────")
    df_li = fetch_linkedin_indeed_jobs()

    print("\n── STEP 2: Naukri (RSS Feed) ─────────────────────────")
    df_naukri = fetch_naukri_jobs()

    frames = [df for df in [df_li, df_naukri] if not df.empty]
    if not frames:
        print("\n⚠️  No jobs returned from any portal.")
        return

    all_jobs = pd.concat(frames, ignore_index=True)
    print(f"\n📦 Total fetched: {len(all_jobs)} jobs\n")

    print("── STEP 3: Filter new + AI analysis ─────────────────")
    new_jobs = []
    for _, row in all_jobs.iterrows():
        uid = f"{row.get('title','')}_{row.get('company','')}".lower().replace(" ", "_")
        if uid not in seen:
            seen.add(uid)
            d = row.to_dict()
            print(f"  🤖 [{d.get('_source')}] {d.get('title')} @ {d.get('company')}")
            d["ai_analysis"] = analyse_job_fit(
                title       = str(d.get("title", "")),
                company     = str(d.get("company", "")),
                description = str(d.get("description", "")),
            )
            new_jobs.append(d)

    print(f"\n── STEP 4: Email ─────────────────────────────────────")
    print(f"  🆕 New jobs: {len(new_jobs)}")
    send_email(new_jobs)

    save_seen_jobs(seen)
    print("\n✅ Done.\n")


if __name__ == "__main__":
    main()
