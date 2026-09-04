# 🎯 AI Resume & Job Fit Matcher

An AI-powered tool that analyzes candidate resumes against specific Job Descriptions (JDs), extracts key technical skills, identifies missing competencies, and generates actionable recommendations and interview preparation questions.

Built using **Python**, **Streamlit**, and **Google Gemini API**.

---

## 🌟 Key Features

- **Resume Parsing**: Seamlessly extracts text from PDF resumes using `pypdf` or direct text input.
- **Pre-Loaded Role JDs**: Instant testing against real Job Descriptions (e.g., AI Developer Intern, Full Stack Developer Intern).
- **Intelligent Match Score**: Calculates overall job-fit percentage (0–100%) based on required skills and candidate experience.
- **Skills Gap Analysis**: Displays matched skills (green badges) and highlights critical missing keywords (yellow badges).
- **Actionable Feedback**: Recruiter-style summary advising on resume improvements.
- **Custom Interview Questions**: Tailored technical questions based on the target role to help prepare for interviews.
- **Hybrid AI Engine**: Integrates with Google Gemini API (`gemini-2.5-flash`), with a built-in offline heuristic fallback when no API key is set.

---

## 🛠️ Tech Stack

- **Frontend / UI**: [Streamlit](https://streamlit.io/)
- **Programming Language**: Python 3.10+
- **AI & LLM**: Google Gemini API (`google-genai`)
- **PDF Extraction**: `pypdf`

---

## 🚀 Quickstart Guide

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ai-job-matcher.git
cd ai-job-matcher
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
streamlit run app.py
```

Open your browser and navigate to `http://localhost:8501`.

---

## 🔑 Getting an API Key (Optional)

1. Visit [Google AI Studio](https://aistudio.google.com/).
2. Click **Create API Key** (Free).
3. Paste the key in the sidebar of the application or set it in your environment:
   ```bash
   export GEMINI_API_KEY="your-key-here"  # Linux/Mac
   set GEMINI_API_KEY="your-key-here"     # Windows CMD
   $env:GEMINI_API_KEY="your-key-here"   # Windows PowerShell
   ```

---

## 💡 Designed For
Candidate preparation for campus recruitment drives, internships, and technical placement rounds.
