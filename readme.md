# 📄 AI Resume Analyzer & Interview Assistant

> An AI-powered all-in-one tool built with **Streamlit and Google Gemini API** that analyzes your resume against a job description — giving ATS score, missing skills, improvement tips, and tailored interview questions instantly.

---

## 📌 Project Overview

Job hunting is tough — especially when you don't know if your resume will even pass the ATS filter. This tool solves that by acting as your **personal AI career coach**: paste your job description, upload your resume, and get a full analysis in seconds.

---

## ✨ Features

- 📤 Upload resume as a **PDF file**
- 📋 Paste any **Job Description** to match against
- 🧠 **AI-powered analysis** using Google Gemini 1.5 Flash
- 📊 **ATS Match Score** out of 100
- 📝 **Resume Summary** — quick overview of your profile
- ❌ **Missing Skills** — what the JD requires that your resume lacks
- ✅ **Suggested Improvements** — actionable tips to strengthen your resume
- 🎤 **Interview Questions** — role-specific questions generated from your resume & JD

---

## 🏗️ How It Works

```
Upload Resume PDF
        ↓
PyPDF2  →  Extract text from all PDF pages
        ↓
Paste Job Description
        ↓
Gemini 1.5 Flash  →  Analyze Resume vs JD with custom prompt
        ↓
Returns:
  1. Resume Summary
  2. ATS Match Score (out of 100)
  3. Missing Skills
  4. Suggested Improvements
  5. Interview Questions
        ↓
Results displayed in Streamlit UI
```

---

## 📂 Project Structure

```
ai-resume-analyzer-interview-assistant/
│
├── streamlit_app.py       # Main application
├── requirements.txt       # Python dependencies
├── resume-ui.jpeg         # App UI screenshot
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| 🖥️ Frontend / UI | Streamlit |
| 📄 PDF Text Extraction | PyPDF2 |
| 🤖 AI Model | Google Gemini 1.5 Flash |
| 🔗 AI SDK | google-generativeai |
| 🔐 Env Management | python-dotenv |

---

## 🖼️ App UI

![Resume Analyzer UI](resume-ui.jpeg)

---

## ▶️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/kartheek-r/ai-resume-analyzer-interview-assistant.git
cd ai-resume-analyzer-interview-assistant
```

### 2. Create a Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Key
Create a `.env` file in the root folder:
```
GOOGLE_API_KEY=your_google_gemini_api_key_here
```
> 🔑 Get your free API key at [Google AI Studio](https://aistudio.google.com/)

### 5. Run the App
```bash
streamlit run streamlit_app.py
```

---

## 📦 Requirements

```
streamlit
google-generativeai
python-dotenv
PyPDF2
```

---

## 📊 Sample Output

After clicking **"Analyze Resume"**, you get:

| Section | What You Get |
|---------|-------------|
| 📝 Resume Summary | A concise overview of your profile |
| 🎯 ATS Match Score | Score out of 100 vs the job description |
| ❌ Missing Skills | Skills in the JD not found in your resume |
| ✅ Suggested Improvements | Actionable tips to improve your resume |
| 🎤 Interview Questions | Role-specific questions based on your resume & JD |

---

## 💡 Use Cases

- 🎓 Freshers tailoring resumes for specific job roles
- 💼 Job seekers optimizing resumes for ATS systems
- 🔄 Career switchers identifying skill gaps
- 🧑‍💼 Anyone who wants to prepare for interviews smartly

---

## 🔮 Future Scope

- 📄 Generate a **Cover Letter** based on resume + JD
- 💬 **Chat mode** — ask follow-up questions about your resume
- 📊 Visual ATS score dashboard with charts
- 🌐 Deploy on **Streamlit Cloud** for public access
- 📥 Export analysis results as a **PDF report**

---

## 🙌 Conclusion

This project combines **PDF parsing** and **generative AI** to create a practical tool that helps job seekers understand exactly where they stand against any job description — and what to do about it. Built as a fresher looking for a job, this tool reflects a real problem solved with real AI.

---

## 👨‍💻 Author

**Ryalampadu Kartheek**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kartheek-ryalampadu)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:kartheekryalampadu@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/kartheek-r)
