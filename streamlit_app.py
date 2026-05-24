import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader

# Load API Key
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash-latest")

st.set_page_config(page_title="AI Resume Analyzer")

st.title("📄 AI Resume Analyzer & Interview Assistant")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if uploaded_file is not None:

    pdf_reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in pdf_reader.pages:
        resume_text += page.extract_text()

    st.success("Resume Uploaded Successfully!")

    if st.button("Analyze Resume"):

        prompt = f"""
        You are an AI Resume Analyzer.

        Resume:
        {resume_text}

        Job Description:
        {job_description}

        Give:
        1. Resume Summary
        2. ATS Match Score out of 100
        3. Missing Skills
        4. Suggested Improvements
        5. Interview Questions
        """

        response = model.generate_content(prompt)

        st.subheader("Analysis Result")

        st.write(response.text)