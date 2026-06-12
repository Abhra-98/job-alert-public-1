# ============================================================
#   config.py — YOUR PERSONAL CONFIGURATION
#
#   WHAT TO EDIT:
#   1. Paste your resume in RESUME_TEXT
#   2. Set your Gmail in EMAIL_SENDER / EMAIL_RECEIVER
#   3. Add/remove job searches in JOB_SEARCHES
#   4. Add/remove Naukri URLs in NAUKRI_SEARCHES
# ============================================================


# ────────────────────────────────────────────────────────
#  YOUR RESUME
#  Paste the full plain text of your resume below.
#  The AI uses this to analyse your fit for each new job.
# ────────────────────────────────────────────────────────
RESUME_TEXT = """
ABHRANIL DAS

Data Analyst | BFSI Domain | 4+ Years Experience
Phone: +91 7003351602
Email: das.abhra10426@gmail.com
LinkedIn: linkedin.com/in/abhranil-das
GitHub: github.com/Abhra-98
Location: Kolkata, India

SUMMARY
BFSI Data Analyst with 4+ years at TCS, driving 15%+ YoY revenue growth across Diligenta Phoenix portfolios in UK Life, Annuity & Pensions. Built 50+ dashboards in Power BI (DAX) and Tableau on GCP BigQuery and Snowflake, with Informatica and dbt pipelines at 98%+ data accuracy. Leveraged Generative AI and Prompt Engineering (ChatGPT, Claude, Gemini, Copilot) with n8n AI agents to cut manual reporting effort by ~30%. Strong in PL/SQL, Python, A/B Testing, Statistical & Dimensional Modelling on Agile/Scrum delivery. Microsoft Power BI Certified | Generative AI Certified        

SKILLS
Languages & Databases:
Python (Pandas, NumPy, Matplotlib, Seaborn, scikit-learn), SQL, PL-SQL (CTEs, Window Functions, Query Optimisation), MS Excel (Advanced, Power Query, Pivot Tables)

Data Engineering / ETL:
Informatica PowerCenter, dbt (Data Build Tool), PySpark, Apache Spark, ETL/ELT Pipelines, Incremental load, Full-Load, Data Preprocessing, Data Cleaning, Data Transformation, Data Pre-processing, Data Quality Framework, OLTP / OLAP, REST API Integration

Cloud & Data Warehousing:
GCP BigQuery, Snowflake, Google Cloud Platform, GCP, AWS, Data Bricks, Data Lakehouse Architecture, Data Contracts, Data Mesh, Data Governance.

BI & Visualisation:
Power BI (DAX), DAX function, Tableau Desktop, Tableau Cloud, Tableau Server, Looker, Metabase, Database, Dashboard Design, Optimisation, KPI Reporting, Data Storytelling, Executive Dashboards

Analytics & Statistical Methods:
Exploratory Data Analysis (EDA), Statistical Modelling, Regression Analysis,  Statistical Analysis, Hypothesis Testing, A/B Testing, Predictive Analytics, Forecasting, Data Mining.

Data Modelling:
Star Schema, Snowflake Schema, Fact & Dimension Tables, Slow Changing Dimension, SCD Type 1 & 2, Dimensional Modelling, Data Contracts, Data Mesh, Data Warehouse.

AI & Generative AI:
Generative AI, Prompt Engineering, Artificial Intelligence, AI Agents, Vector DB, Tokenization , Indexing, Vector Embeddings, Neural Network, MCP, AI/ML, MLOps, RAG pipelines, Fine-Tuning, AGI, ASI, VLM, Reinforcement Learning, LLM, ChatGPT, Claude, Gemini, GitHub Copilot, Agentic AI, n8n Automation.

Domain & Methodology:
BFSI, UK Life Insurance, Annuity, Pension, Claims Processing, Agile Scrum, Sprint Planning, Stakeholder Communications, KPI Definition & Tracking, UK BFSI Ticket Reportings, 

WORK EXPERIENCE
Tata Consultancy Services
Role: Data Analyst
Project: Diligenta Phoenix, UK BFSI
Location: Kolkata, India
Apr 2023 - Present

Built 50+ Tableau and Power BI dashboards with advanced SQL analytics, driving 25% + YoY revenue uplift across UK life insurance and pension portfolios.

Built dashboards analysing 120K HMRC tax regime records across PAYE and Self-Assessment, detecting 7% fault-prone cohort representing £6.2M in misclassified tax liability.

Integrated Gen AI and Prompt Engineering Copilot, ChatGPT into workflows, reducing manual reporting effort by 30% while maintaining Agile/Scrum and governance standards.

iMerit Technology Services
Role: Data Annotator - AI and ML
Project: Cruise Robotaxi (General Motors) 
Location: Kolkata, India
Sep 2021 - Feb 2023

Delivered 200+ high-precision annotation tasks (semantic segmentation, object detection, 3D point cloud labelling).

Built large-scale AI training datasets using image, video, and LiDAR annotation for autonomous vehicle ML/DL pipelines.

Optimised SQL query from 4 minutes to 4 seconds (60× improvement) using CTEs, reducing batch runtime by 38 minutes.

KEY PROJECTS
AI Automation Job Alert Agent - GitHub
Python |JobSpy | Pandas | Google Gemini API | Gmail SMTP | GitHub Actions
Built a fully automated job alert system scraping LinkedIn, Indeed, Naukri.
Processes ~150–200 jobs/day and scores 10+ job-fit dimensions hourly.
Reduced manual job-hunting effort by ~90%.

WhatsApp AI Automation Bot
n8n | Gemini AI | Google Sheets | Meta WhatsApp API
Developed a 24/7 AI bot for inventory analytics and order management.
Eliminated missed sales and reduced response time to near zero.

Tableau HR Analytics Dashboard
Tableau Cloud, ChatGPT, Figma, Draw.io    
Built dashboard covering 8,950 employees across 15 charts.
Identified ~25% female PhD pay gap and fixed 966 data anomalies.


EDUCATION
Techno International Newtown, Kolkata, India (2017 – 2021)
Bachelor of Technology — Mechanical Engineering
DGPA: 8.32/10

CERTIFICATIONS
Microsoft Certified: Power BI Data Analyst Associate PL 300
Cert. ID: 1C8694-7EV5D9  Cand. ID: MS0996855095

Generative AI for Data Engineering and Data Professionals - Udemy
Cert. ID: UC-885a0051

ACHIEVEMENTS
Star Team Award — TCS (Outstanding project delivery & BI contribution).
Special Initiative Award (HR) — Diligenta Phoenix dashboard innovation.
Drove 25%+ YoY revenue uplift through data insights.
Reduced manual reporting effort by ~30% using AI workflows. """

# ────────────────────────────────────────────────────────
#  LINKEDIN & INDEED JOB SEARCHES
#
#  site options : "linkedin"  or  "indeed"
#  search_term  : Keywords to search (same as typing in the search bar)
#  location     : City, state, or "India" for all India
#  results_wanted: How many jobs to fetch per search (max 20 recommended)
# ────────────────────────────────────────────────────────
JOB_SEARCHES = [

    # ── LinkedIn ───────────────────────────────────────
    {
        "site"           : "linkedin",
        "search_term"    : "Data Analyst",
        "location"       : "India",
        "results_wanted" : 10,
    },
    {
        "site"           : "linkedin",
        "search_term"    : "Data Analyst",
        "location"       : "Kolkata",
        "results_wanted" : 10,
    },
    {
        "site"           : "linkedin",
        "search_term"    : "Business Analyst",
        "location"       : "India",
        "results_wanted" : 10,
    },
    {
        "site"           : "linkedin",
        "search_term"    : "Data Engineer",
        "location"       : "Kolkata",
        "results_wanted" : 10,
    },
    {
        "site"           : "linkedin",
        "search_term"    : "Data Scientist",
        "location"       : "India",
        "results_wanted" : 10,
    },
    {
        "site"           : "linkedin",
        "search_term"    : "Tableau Developer",
        "location"       : "India",
        "results_wanted" : 10,
    },
    {
        "site"           : "linkedin",
        "search_term"    : "Power BI Developer",
        "location"       : "India",
        "results_wanted" : 10,
    },
    {
        "site"           : "linkedin",
        "search_term"    : "Tableau Developer",
        "location"       : "Kolkata",
        "results_wanted" : 10,
    },
    {
        "site"           : "linkedin",
        "search_term"    : "Software Developer",
        "location"       : "Kolkata",
        "results_wanted" : 5,
    },
    {
        "site"           : "linkedin",
        "search_term"    : "Software Developer",
        "location"       : "India",
        "results_wanted" : 5,
    },
    {
        "site"           : "linkedin",
        "search_term"    : "PL/SQL Developer",
        "location"       : "India",
        "results_wanted" : 10,
    },
    {
        "site"           : "linkedin",
        "search_term"    : "SQL Developer",
        "location"       : "India",
        "results_wanted" : 10,
    },
     {
        "site"           : "linkedin",
        "search_term"    : "SENIOR ENGINEER",
        "location"       : "India",
        "results_wanted" : 10,
    },
    
    # ── Indeed ─────────────────────────────────────────
    {
        "site"           : "indeed",
        "search_term"    : "Data Analyst",
        "location"       : "India",
        "results_wanted" : 5,
    },
    {
        "site"           : "indeed",
        "search_term"    : "SQL Developer",
        "location"       : "India",
        "results_wanted" : 5,
    },
    {
        "site"           : "indeed",
        "search_term"    : "PL/SQL Developer",
        "location"       : "India",
        "results_wanted" : 5,
    },
    {
        "site"           : "indeed",
        "search_term"    : "Power BI Developer",
        "location"       : "India",
        "results_wanted" : 5,
    },
    {
        "site"           : "indeed",
        "search_term"    : "Tableau Developer",
        "location"       : "India",
        "results_wanted" : 5,
    },
   
    {
        "site"           : "indeed",
        "search_term"    : "Data Analyst",
        "location"       : "Kolkata",
        "results_wanted" : 5,
    }
]


# ────────────────────────────────────────────────────────
#  NAUKRI JOB SEARCHES
#
#  HOW TO GET YOUR NAUKRI URL:
#  1. Open naukri.com in your browser
#  2. Search for a role (e.g. "Data Analyst") + location
#  3. Copy the URL from your browser address bar
#  4. Paste it as a new entry below
#
#  URL EXAMPLES:
#  https://www.naukri.com/data-analyst-jobs
#  https://www.naukri.com/data-analyst-jobs-in-kolkata
#  https://www.naukri.com/business-analyst-jobs-in-india
#  https://www.naukri.com/data-scientist-jobs
# ────────────────────────────────────────────────────────
NAUKRI_SEARCHES = [
    {
        "keyword"  : "Data Analyst",
        "location" : "India",
        "label"    : "Data Analyst — All India",
    },
    {
       "keyword"  : "Data Analyst",
        "location" : "kolkata",
        "label"    : "Data Analyst — Kolkata",
    },
    {
        "keyword"  : "Analytics",
        "location" : "kolkata",
        "label"    : "Analytics — Kolkata",
    },
    {
        "keyword"  : "Analytics",
        "location" : "India",
        "label"    : "Analytics — All India",
    },
    {
        "keyword"  : "Data Analytics",
        "location" : "India",
        "label"    : "Data Analytics — All India",
    },
    {
        "keyword"  : "PL/SQL Developer",
        "location" : "India",
        "label"    : "PL/SQL Developer — All India",
    },
    {
        "keyword"  : "PL/SQL Developer",
        "location" : "Kolkata",
        "label"    : "PL/SQL Developer— Kolkata",  
    },
    {
        "keyword"  : "SQL Developer",
        "location" : "India",
        "label"    : "SQL Developer — All India",
    },
    {
        "keyword"  : "SQL Developer",
        "location" : "Kolkata",
        "label"    : "SQL Developer — Kolkata",
    }
]


# ────────────────────────────────────────────────────────
#  YOUR EMAIL SETTINGS
#  Use your Gmail address for both.
#  Alerts will be sent from and received at this address.
# ────────────────────────────────────────────────────────
EMAIL_SENDER   = "das.abhra10498@gmail.com"    # ← Change this
EMAIL_RECEIVER = "das.abhra10498@gmail.com"    # ← Change this


# ────────────────────────────────────────────────────────
#  ⚠️  DO NOT put your passwords or API keys here.
#  GMAIL_APP_PASSWORD and GEMINI_API_KEY are stored
#  securely in GitHub Secrets — see setup guide.
# ────────────────────────────────────────────────────────
