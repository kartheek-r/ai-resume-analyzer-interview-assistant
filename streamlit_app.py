import os
import re
import streamlit as st
from google import genai
from pydantic import BaseModel
from pypdf import PdfReader

MODEL = "gemini-3.5-flash"

SKILLS = [
    "python", "java", "javascript", "sql", "mysql", "postgresql", "mongodb",
    "pandas", "numpy", "matplotlib", "scikit-learn", "tensorflow", "pytorch",
    "machine learning", "deep learning", "nlp", "llm", "generative ai",
    "prompt engineering", "rag", "embeddings", "vector database", "faiss",
    "langchain", "hugging face", "streamlit", "flask", "fastapi", "django",
    "docker", "kubernetes", "git", "github", "aws", "azure", "gcp", "linux",
    "power bi", "tableau", "excel", "data analysis", "data visualization",
    "statistics", "etl", "spark", "hadoop", "rest api", "html", "css",
    "react", "node.js", "opencv", "data structures", "algorithms", "oop",
    "ci/cd", "agile",
]


class Analysis(BaseModel):
    summary: str
    llm_match_score: int
    missing_skills: list[str]
    improvements: list[str]
    interview_questions: list[str]


st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")
st.title("📄 AI Resume Analyzer & Interview Assistant")


def get_api_key():
    try:
        return st.secrets["GOOGLE_API_KEY"]
    except Exception:
        return os.getenv("GOOGLE_API_KEY")


api_key = get_api_key()
if not api_key:
    st.error("Set GOOGLE_API_KEY in Streamlit Secrets or as an environment variable.")
    st.stop()

client = genai.Client(api_key=api_key)


def extract_text(file):
    reader = PdfReader(file)
    return "\n".join((p.extract_text() or "") for p in reader.pages).strip()


def find_skills(text):
    t = text.lower()
    return {
        s for s in SKILLS
        if re.search(r"(?<![a-z0-9])" + re.escape(s) + r"(?![a-z0-9])", t)
    }


uploaded = st.file_uploader("Upload Resume PDF", type=["pdf"])
jd = st.text_area("Paste Job Description", height=200)

if st.button("Analyze Resume", type="primary"):
    if not uploaded:
        st.warning("Please upload your resume PDF.")
        st.stop()
    if len(jd.strip()) < 30:
        st.warning("Please paste a job description.")
        st.stop()

    resume_text = extract_text(uploaded)
    if not resume_text:
        st.error("No text found in this PDF. It may be a scanned image.")
        st.stop()

    required = find_skills(jd)
    have = find_skills(resume_text)
    matched = sorted(required & have)
    kw_missing = sorted(required - have)
    kw_score = round(100 * len(matched) / len(required)) if required else None

    prompt = f"""You are an expert resume reviewer and technical interviewer.
Compare the resume with the job description.

Resume:
{resume_text}

Job Description:
{jd}

Return:
- summary: 2-3 sentence profile summary
- llm_match_score: integer 0-100 for how well the resume fits the job
- missing_skills: skills the job needs that the resume lacks
- improvements: 5 specific, actionable resume improvements
- interview_questions: 8 role-specific interview questions
"""

    with st.spinner("Analyzing..."):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt,
                config={
                    "response_mime_type": "application/json",
                    "response_schema": Analysis,
                },
            )
            analysis = response.parsed or Analysis.model_validate_json(response.text)
        except Exception as e:
            st.error(f"Gemini error: {e}")
            st.stop()

    ai_score = max(0, min(100, analysis.llm_match_score))
    final = round(0.6 * kw_score + 0.4 * ai_score) if kw_score is not None else ai_score

    st.session_state["result"] = {
        "analysis": analysis,
        "ai": ai_score,
        "kw": kw_score,
        "final": final,
        "matched": matched,
        "kw_missing": kw_missing,
    }

r = st.session_state.get("result")
if r:
    a = r["analysis"]
    c1, c2, c3 = st.columns(3)
    c1.metric("Final match", f"{r['final']}%")
    c2.metric("Keyword match", f"{r['kw']}%" if r["kw"] is not None else "n/a")
    c3.metric("AI score", f"{r['ai']}%")
    st.progress(r["final"] / 100)
    st.caption("Final = 60% keyword match (computed in code) + 40% AI score.")

    t1, t2, t3, t4 = st.tabs(["Summary", "Skills", "Improvements", "Interview"])
    with t1:
        st.write(a.summary)
    with t2:
        st.subheader("✅ Matched (keyword check)")
        st.write(", ".join(r["matched"]) or "None found")
        st.subheader("❌ Missing (keyword check)")
        st.write(", ".join(r["kw_missing"]) or "None")
        st.subheader("❌ Missing (AI view)")
        for s in a.missing_skills:
            st.write(f"- {s}")
    with t3:
        for i in a.improvements:
            st.write(f"- {i}")
    with t4:
        for n, q in enumerate(a.interview_questions, 1):
            st.write(f"{n}. {q}")

    report = (
        f"# Resume Analysis\n\nFinal match: {r['final']}%\n"
        f"Keyword: {r['kw']}% | AI: {r['ai']}%\n\n"
        f"## Summary\n{a.summary}\n\n## Missing skills\n"
        + "\n".join(f"- {s}" for s in a.missing_skills)
        + "\n\n## Improvements\n"
        + "\n".join(f"- {i}" for i in a.improvements)
        + "\n\n## Interview questions\n"
        + "\n".join(f"{n}. {q}" for n, q in enumerate(a.interview_questions, 1))
    )
    st.download_button("⬇️ Download report", report, "resume_analysis.md")
