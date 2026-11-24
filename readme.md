# 📄 AI Resume Analyzer & Interview Assistant

🔗 **Live Demo:** https://ai-resume-analyzer-interview-assistant-8uhvqxhrtcvvgbyktoq95v.streamlit.app/

> Upload your resume, paste a job description, and get a match score, skill gaps, improvement tips, and tailored interview questions. The score combines a **keyword check computed in code** with an **AI score from Gemini**, so it isn't just an LLM guess.

---

## 📌 Overview

Most resume tools ask an LLM for a score and trust whatever comes back. This project uses two signals instead:

1. **Keyword match (deterministic):** skills found in the job description are checked against the resume in code. It is repeatable and explainable.
2. **AI score (Gemini):** judges overall fit, including context that keywords miss.

The final score is **60% keyword match + 40% AI score**. The AI response uses **structured output** (a JSON schema validated with Pydantic), so the results always arrive in a predictable format.

## ✨ Features

- 📤 Upload a resume as a PDF
- 📋 Paste any job description
- 📊 **Three scores:** final match, keyword match, and AI score
- ✅ Matched skills and ❌ missing skills from the keyword check
- 🧠 Missing skills and gaps from the AI's point of view
- 🛠️ Five specific resume improvement suggestions
- 🎤 Eight role-specific interview questions based on your resume and the job description
- ⬇️ Downloadable analysis report
- ☁️ Deployed on Streamlit Cloud

## 🏗️ How It Works

```
Resume PDF → pypdf → resume text
Job description (pasted)
        ↓
Keyword check in code (skill list + regex)
   → matched skills, missing skills, keyword score
        ↓
Gemini 3.5 Flash with a JSON schema (Pydantic)
   → summary, AI score, missing skills, improvements, interview questions
        ↓
Final score = 0.6 × keyword + 0.4 × AI
        ↓
Dashboard with tabs + downloadable report
```

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| UI | Streamlit |
| PDF text extraction | pypdf |
| LLM | Google Gemini 3.5 Flash (`google-genai` SDK) |
| Structured output | Pydantic + Gemini response schema |
| Keyword scoring | Python `re` (regex) |
| Hosting | Streamlit Cloud |

## 🖼️ Screenshots

**Score dashboard**

![Score dashboard](demo1.jpg)

**Skills analysis (keyword check + AI view)**

![Skills analysis](demo2.jpg)

**Tailored interview questions**

![Interview questions](demo3.jpg)

## ▶️ Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/kartheek-r/ai-resume-analyzer-interview-assistant.git
cd ai-resume-analyzer-interview-assistant
```

**2. Create a virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your API key**

Get a free key from [Google AI Studio](https://aistudio.google.com/), then create `.streamlit/secrets.toml`:
```toml
GOOGLE_API_KEY = "your_key_here"
```
(Or set an environment variable named `GOOGLE_API_KEY`.)

**5. Run**
```bash
streamlit run streamlit_app.py
```

## ☁️ Deploy on Streamlit Cloud

1. Push the repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) → **Create app**
3. Select the repo, branch `main`, main file `streamlit_app.py`
4. Under **Advanced settings → Secrets**, add `GOOGLE_API_KEY = "your_key_here"`
5. Deploy

## ⚠️ Limitations

- Works with text-based PDFs only (scanned resumes need OCR)
- The keyword check only knows the skills in the built-in skill list
- The AI score can vary slightly between runs

## 🔮 Future Improvements

- Embedding-based skill matching, so related terms count (for example "vector search" and "vector database")
- Cover letter generator
- PDF export of the report
- Support for multiple job descriptions at once

## 👨‍💻 Author

**Ryalampadu Kartheek**
[LinkedIn](https://www.linkedin.com/in/kartheek-ryalampadu) · [GitHub](https://github.com/kartheek-r)
