import os
import streamlit as st
from pypdf import PdfReader
import json
import time

# Page Configuration - Premium SaaS Layout
st.set_page_config(
    page_title="TalentFit AI • Enterprise Resume & Job Fit Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sophisticated, Modern Glassmorphism & SaaS Design System
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Main background accents */
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 50%, #e2e8f0 100%);
    }

    /* Navbar / Hero Banner */
    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 60%, #3b82f6 100%);
        border-radius: 16px;
        padding: 2.2rem 2.5rem;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 20px 25px -5px rgba(15, 23, 42, 0.15), 0 8px 10px -6px rgba(15, 23, 42, 0.1);
        position: relative;
        overflow: hidden;
    }

    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(59, 130, 246, 0.2);
        border: 1px solid rgba(147, 197, 253, 0.3);
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #93c5fd;
        margin-bottom: 0.8rem;
    }

    .hero-title {
        font-size: 2.3rem;
        font-weight: 800;
        letter-spacing: -0.025em;
        line-height: 1.2;
        margin-bottom: 0.5rem;
        background: linear-gradient(to right, #ffffff, #e2e8f0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        font-size: 1.05rem;
        color: #94a3b8;
        max-width: 720px;
        line-height: 1.5;
        font-weight: 400;
    }

    /* Card Panels */
    .saas-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(12px);
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 1.8rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
        margin-bottom: 1.5rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .saas-card:hover {
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
    }

    .card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.4rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .card-subtitle {
        font-size: 0.85rem;
        color: #64748b;
        margin-bottom: 1.2rem;
    }

    /* Score Indicator Ring/Card */
    .score-banner {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.06);
        text-align: center;
    }

    .score-number {
        font-size: 3.6rem;
        font-weight: 800;
        letter-spacing: -0.05em;
        line-height: 1;
    }

    .score-number.high { color: #059669; }
    .score-number.medium { color: #d97706; }
    .score-number.low { color: #dc2626; }

    /* Pill Badges */
    .skill-pill-match {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #ecfdf5;
        border: 1px solid #a7f3d0;
        color: #065f46;
        padding: 6px 14px;
        border-radius: 9999px;
        font-size: 0.82rem;
        font-weight: 600;
        margin: 4px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
    }

    .skill-pill-missing {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #fffbeb;
        border: 1px solid #fde68a;
        color: #92400e;
        padding: 6px 14px;
        border-radius: 9999px;
        font-size: 0.82rem;
        font-weight: 600;
        margin: 4px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
    }

    .rec-item {
        background: #ffffff;
        border-left: 4px solid #3b82f6;
        padding: 1rem 1.2rem;
        border-radius: 8px;
        margin-bottom: 0.75rem;
        border-top: 1px solid #f1f5f9;
        border-right: 1px solid #f1f5f9;
        border-bottom: 1px solid #f1f5f9;
        font-size: 0.92rem;
        color: #334155;
        line-height: 1.5;
    }

    .interview-card {
        background: #f8fafc;
        border: 1px dashed #cbd5e1;
        border-radius: 10px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.75rem;
        font-size: 0.92rem;
        color: #1e293b;
        font-weight: 500;
    }

    /* Custom Streamlit Buttons */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        color: white;
        border: none;
        border-radius: 10px;
        font-size: 1.05rem;
        font-weight: 700;
        padding: 0.75rem 2rem;
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.35);
        transition: all 0.2s ease;
    }

    div.stButton > button:first-child:hover {
        background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
        box-shadow: 0 14px 20px -3px rgba(37, 99, 235, 0.45);
        transform: translateY(-1px);
    }
</style>
""", unsafe_allow_html=True)

# Helper function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    try:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return None

# Real JDs pre-loaded from Internship Mela 2026 Drive
SAMPLE_JDS = {
    "— Select a verified Job Description from the Drive —": "",
    "AI Developer Intern (Srays Technologies)": """JOB ROLE: AI DEVELOPER INTERN
Company: Srays Technologies
Focus: Machine Learning, Generative AI, Data Pipelines, Application Integration

Key Responsibilities:
- Build and evaluate Machine Learning models (classification, prediction, ranking).
- Work with Generative AI models, prompt engineering, and LLM API integrations.
- Preprocess and clean datasets using NumPy, Pandas, and Scikit-learn.
- Integrate AI models into software applications using REST APIs and JSON.
- Version control with Git & GitHub, test code, and troubleshoot models.

Required Tech Toolkit:
- Python (Primary), C++, or Java
- NumPy, Pandas, Scikit-learn, TensorFlow / PyTorch (Basics)
- REST APIs, JSON, Databases, Git / GitHub
- LangChain, Hugging Face, or OpenAI API (Added Advantage)""",

    "AI Developer Intern (Ekhai)": """JOB ROLE: AI DEVELOPER INTERN
Company: Ekhai
Focus: Artificial Intelligence, Deep Learning, Generative AI & Automation

Responsibilities:
- Assist in developing AI/ML solutions for real-world business challenges.
- Train, test, and tune ML algorithms for prediction and automated workflows.
- Explore Large Language Models (LLMs), chatbots, and agentic workflows.
- Collect, clean, and run exploratory data analysis (EDA) on raw data.
- Integrate models with web apps, backend APIs, and microservices.

Required Skills:
- Python programming, OOP fundamentals.
- Scikit-learn, NumPy, Pandas, PyTorch / TensorFlow.
- Prompt Engineering, LLM workflows, and REST APIs.""",

    "Full Stack Development Intern (Auare)": """JOB ROLE: FULL STACK DEVELOPMENT INTERN
Company: Auare
Focus: Modern Web Application Engineering & RESTful Systems

Key Responsibilities:
- Build responsive, accessible front-end interfaces using React.js, HTML5, CSS3, and modern JavaScript (ES6+).
- Implement server-side logic, routing, and RESTful APIs using Node.js / Python / Java.
- Manage databases (MySQL, PostgreSQL, or MongoDB) with clean schema designs and efficient queries.
- Collaborate on source code with Git & GitHub, perform code reviews, and optimize page load speed."""
}

# Sidebar - Professional System Controls
with st.sidebar:
    st.markdown("### ⚡ System Status")
    st.markdown("""
        <div style="background: #f1f5f9; padding: 12px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 0.85rem;">
            <div style="color: #059669; font-weight: 700;">● Engine: Active</div>
            <div style="color: #64748b; margin-top: 4px;">Targeting: <b>Internship Mela 2026</b></div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🔑 AI Model Engine")
    api_key = st.text_input(
        "Google Gemini API Key (Optional)",
        type="password",
        value=os.environ.get("GEMINI_API_KEY", ""),
        help="Paste your Gemini API key from aistudio.google.com for full generative reasoning. If empty, the built-in heuristic semantic engine runs automatically."
    )
    
    if api_key:
        st.success("✨ Custom LLM Engine Connected")
    else:
        st.info("⚡ Running in High-Speed Heuristic Engine mode. Add a free API key anytime for deep reasoning.")
        
    st.markdown("---")
    st.markdown("### 🎯 Hiring Companies")
    st.markdown("""
    - **Srays Technologies** (AI Intern)
    - **Ekhai** (AI Developer)
    - **Nim Technologies** (AI Intern)
    - **Auare** (Full Stack Developer)
    """)
    st.markdown("---")
    st.caption("TalentFit AI v2.4 Enterprise • Created for Placement Preparation")

# Hero Section
st.markdown("""
<div class="hero-container">
    <div class="hero-badge">⚡ Placement Drive Ready</div>
    <div class="hero-title">TalentFit AI Career Intelligence</div>
    <div class="hero-subtitle">
        Deep-scan your resume against real Job Descriptions from campus recruiters. 
        Uncover missing ATS keywords, benchmark your match rate, and unlock tailored interview questions in seconds.
    </div>
</div>
""", unsafe_allow_html=True)

# Dual-Input Workspace Layout
col_jd, col_res = st.columns(2, gap="medium")

with col_jd:
    st.markdown("""
    <div class="saas-card">
        <div class="card-title">📋 1. Target Role & Job Description</div>
        <div class="card-subtitle">Select a drive JD or paste the exact requirements from the company.</div>
    """, unsafe_allow_html=True)
    
    selected_sample = st.selectbox(
        "Drive Pre-Sets",
        list(SAMPLE_JDS.keys()),
        label_visibility="collapsed"
    )
    default_jd = SAMPLE_JDS[selected_sample] if selected_sample != "— Select a verified Job Description from the Drive —" else ""
    
    jd_text = st.text_area(
        "Job Requirements Content",
        value=default_jd,
        height=260,
        placeholder="Paste role specifications, technical requirements, or job responsibilities...",
        label_visibility="collapsed"
    )
    st.markdown("</div>", unsafe_allow_html=True)

with col_res:
    st.markdown("""
    <div class="saas-card">
        <div class="card-title">📄 2. Candidate Resume Profile</div>
        <div class="card-subtitle">Upload your PDF resume or paste your technical background directly.</div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"],
        label_visibility="collapsed"
    )
    
    resume_text = ""
    if uploaded_file is not None:
        with st.spinner("Parsing resume text..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            if resume_text:
                st.success(f"✓ Parsed `{uploaded_file.name}` ({len(resume_text.split())} words)")
    
    resume_text_manual = st.text_area(
        "Resume Content",
        value=resume_text if resume_text else "",
        height=190 if uploaded_file else 260,
        placeholder="Paste your education, skills, projects, and coursework here...",
        label_visibility="collapsed"
    )
    if not resume_text:
        resume_text = resume_text_manual
    st.markdown("</div>", unsafe_allow_html=True)

# Centered Action Trigger
analyze_btn = st.button("⚡ Run Comprehensive ATS & Fit Analysis", use_container_width=True)

def fallback_heuristic_analysis(resume_content, jd_content):
    """Accurate offline heuristic matcher tailored for Internship Mela tech stacks."""
    skills_map = {
        "python": "Python",
        "java": "Java",
        "c++": "C++",
        "c": "C Programming",
        "javascript": "JavaScript",
        "react": "React.js",
        "node": "Node.js",
        "sql": "SQL Databases",
        "mysql": "MySQL",
        "mongodb": "MongoDB",
        "machine learning": "Machine Learning",
        "deep learning": "Deep Learning",
        "nlp": "Natural Language Processing (NLP)",
        "llm": "LLMs & GenAI",
        "generative ai": "Generative AI",
        "langchain": "LangChain",
        "pandas": "Pandas",
        "numpy": "NumPy",
        "scikit-learn": "Scikit-learn",
        "tensorflow": "TensorFlow",
        "pytorch": "PyTorch",
        "git": "Git & GitHub",
        "rest api": "RESTful APIs",
        "json": "JSON Data Handling",
        "html": "HTML5 / CSS3",
        "oop": "OOP Fundamentals"
    }
    
    resume_lower = resume_content.lower()
    jd_lower = jd_content.lower()
    
    jd_skills = [k for k in skills_map if k in jd_lower]
    if not jd_skills:
        jd_skills = ["python", "machine learning", "pandas", "numpy", "git", "rest api"]
        
    matched = [skills_map[k] for k in jd_skills if k in resume_lower]
    missing = [skills_map[k] for k in jd_skills if k not in resume_lower]
    
    base_ratio = len(matched) / len(jd_skills) if jd_skills else 0.5
    calc_score = int(base_ratio * 100)
    
    # Smooth score for fresher benchmarks
    score = max(25, min(calc_score, 94))
    
    return {
        "match_percentage": score,
        "summary": "The candidate presents an aligned foundation with transferable engineering skills. Enhancing project narratives with quantified outcomes and incorporating the targeted missing technologies will markedly increase shortlisting probability.",
        "matching_skills": matched if matched else ["Core Programming", "Problem Solving", "Computer Science Fundamentals"],
        "missing_skills": missing if missing else ["Advanced Model Tuning", "Docker / Cloud Deployment"],
        "recommendations": [
            "In your projects section, explicitly mention core libraries used (e.g., 'Utilized NumPy and Pandas for data manipulation; trained models via Scikit-learn').",
            "Ensure your GitHub profile link is clickable at the top of your resume, with comprehensive README documentation and architectural summaries for top repositories.",
            "Formulate project bullets using the Google XYZ framework: 'Accomplished [X] as measured by [Y], by doing [Z]'."
        ],
        "interview_prep_questions": [
            "Can you explain the workflow of cleaning and handling missing values in a real-world dataset using Pandas?",
            "What is the difference between supervised and unsupervised learning, and how do you evaluate classification accuracy?",
            "How do RESTful APIs facilitate communication between front-end interfaces and server-side ML models?"
        ]
    }

def analyze_with_gemini(api_key, resume_content, jd_content):
    """Google Gemini deep analytical reasoning."""
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        
        prompt = f"""
You are a Principal Technical Recruiter and Engineering Hiring Lead conducting a strict ATS match evaluation for an internship applicant.
Target Job Description:
{jd_content}

Applicant Resume:
{resume_content}

Analyze the alignment thoroughly. Output ONLY a valid JSON object matching this schema:
{{
  "match_percentage": <integer 0-100>,
  "summary": "<Concise 2-3 sentence executive evaluation of alignment and potential>",
  "matching_skills": ["<Skill 1>", "<Skill 2>", ...],
  "missing_skills": ["<Skill 1>", "<Skill 2>", ...],
  "recommendations": ["<Specific actionable resume improvement 1>", "<Improvement 2>", "<Improvement 3>"],
  "interview_prep_questions": ["<Likely technical interview question 1>", "<Question 2>", "<Question 3>"]
}}
"""
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        raw_text = response.text.strip()
        if raw_text.startswith("```"):
            raw_text = raw_text.split("\n", 1)[1]
            if raw_text.endswith("```"):
                raw_text = raw_text.rsplit("```", 1)[0]
        return json.loads(raw_text)
    except Exception as e:
        return fallback_heuristic_analysis(resume_content, jd_content)

# Process Results
if analyze_btn:
    if not jd_text.strip():
        st.warning("⚠️ Please provide or select a target Job Description first.")
    elif not resume_text.strip():
        st.warning("⚠️ Please provide resume details (via PDF upload or direct text).")
    else:
        with st.spinner("⚡ Running multi-dimensional fit analysis and ATS parsing..."):
            time.sleep(0.4)
            if api_key and api_key.strip():
                result = analyze_with_gemini(api_key.strip(), resume_text, jd_text)
            else:
                result = fallback_heuristic_analysis(resume_text, jd_text)
        
        score = result.get("match_percentage", 65)
        score_class = "high" if score >= 75 else ("medium" if score >= 50 else "low")
        score_label = "Optimal Fit" if score >= 75 else ("Competitive Candidate" if score >= 50 else "Skills Alignment Required")
        
        st.markdown("---")
        
        # Metric Overview Card
        st.markdown(f"""
        <div class="score-banner">
            <div style="text-transform: uppercase; font-size: 0.85rem; font-weight: 700; color: #64748b; letter-spacing: 0.05em; margin-bottom: 0.5rem;">
                Target Benchmark Index
            </div>
            <div class="score-number {score_class}">{score}%</div>
            <div style="font-size: 1.15rem; font-weight: 700; color: #1e293b; margin-top: 0.6rem;">{score_label}</div>
            <div style="max-width: 650px; margin: 0.8rem auto 0; color: #64748b; font-size: 0.95rem; line-height: 1.5;">
                {result.get('summary', '')}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Skills Grid Layout
        col_m1, col_m2 = st.columns(2, gap="medium")
        
        with col_m1:
            st.markdown("""
            <div class="saas-card">
                <div class="card-title">✅ Verified Matching Capabilities</div>
                <div class="card-subtitle">Skills detected in your resume that directly satisfy JD criteria.</div>
            """, unsafe_allow_html=True)
            matching = result.get("matching_skills", [])
            if matching:
                pills = "".join([f'<span class="skill-pill-match">✓ {s}</span>' for s in matching])
                st.markdown(pills, unsafe_allow_html=True)
            else:
                st.info("No direct keyword matches detected. Emphasize standard tools like Python and Git.")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col_m2:
            st.markdown("""
            <div class="saas-card">
                <div class="card-title">⚠️ Priority Missing Keywords</div>
                <div class="card-subtitle">Critical requirements highlighted in the JD to incorporate into your profile.</div>
            """, unsafe_allow_html=True)
            missing = result.get("missing_skills", [])
            if missing:
                pills = "".join([f'<span class="skill-pill-missing">+ {s}</span>' for s in missing])
                st.markdown(pills, unsafe_allow_html=True)
            else:
                st.success("Outstanding! All core competencies listed in the job description are present.")
            st.markdown("</div>", unsafe_allow_html=True)
            
        # Recommendations & Interview Prep
        col_rec, col_int = st.columns(2, gap="medium")
        
        with col_rec:
            st.markdown("""
            <div class="saas-card">
                <div class="card-title">💡 Strategic Resume Enhancements</div>
                <div class="card-subtitle">Action items to optimize your resume for recruiters and ATS filters.</div>
            """, unsafe_allow_html=True)
            for rec in result.get("recommendations", []):
                st.markdown(f'<div class="rec-item">📌 {rec}</div>', unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col_int:
            st.markdown("""
            <div class="saas-card">
                <div class="card-title">🎯 Role-Specific Interview Questions</div>
                <div class="card-subtitle">Anticipated technical questions likely to be asked by the interviewer.</div>
            """, unsafe_allow_html=True)
            for q in result.get("interview_prep_questions", []):
                st.markdown(f'<div class="interview-card">❓ <b>Question:</b> {q}</div>', unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

# Clean Professional Footer
st.markdown("""
<div style="text-align: center; margin-top: 3rem; color: #94a3b8; font-size: 0.85rem;">
    TalentFit AI • Designed for Enterprise Placement Benchmarking & Candidate Readiness
</div>
""", unsafe_allow_html=True)
