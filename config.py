# ============================================================
#   config.py — PERSONAL DATA CONFIGURATION
# ────────────────────────────────────────────────────────
#  YOUR RESUME = """ Paste your resume Details """
# ────────────────────────────────────────────────────────
#  LINKEDIN & INDEED JOB SEARCHES
#
#  site options : "linkedin"  or  "indeed"
#  search_term  : Keywords to search.
#  location     : City, state, or "India" for all India.
#  results_wanted: How many jobs to fetch per search. 
# ────────────────────────────────────────────────────────
JOB_SEARCHES = [

    # ── LinkedIn ───────────────────────────────────────
    {
        "site"           : "linkedin",
        "search_term"    : "Role",
        "location"       : "India",
        "results_wanted" : 20,
    }
   
    # ── Indeed ─────────────────────────────────────────
    {
        "site"           : "indeed",
        "search_term"    : "Role",
        "location"       : "India",
        "results_wanted" : 5,
    }  
]
# ────────────────────────────────────────────────────────
#  NAUKRI JOB SEARCHES
#  1. Open naukri.com in your browser
#  2. Search for a role (e.g. "Role") + location
#  3. Paste it as a new entry below
#
#  URL EXAMPLES:
#  https://www.naukri.com/Role-jobs-in-location
# ────────────────────────────────────────────────────────
NAUKRI_SEARCHES = [
    {
        "keyword"  : "Role",
        "location" : "India",
        "label"    : "Role — All India",
    }
]

# ────────────────────────────────────────────────────────
#  YOUR EMAIL SETTINGS
# ────────────────────────────────────────────────────────
EMAIL_SENDER   = "****@****.com"    #
EMAIL_RECEIVER = "****@****.com"    # 
