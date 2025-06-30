import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="PDF Critique Summarizer",
    page_icon="📃",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("PDF Critique Summarizer")
st.markdown(
    "upload a PDF and get a summary of the critique"
)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

input_file = st.file_uploader("Upload a PDF", type=["pdf"])
job_role = st.text_input("Enter your job role you're going for")
analyze = st.button("Analyze")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

if analyze and input_file:
    try:
        file_contents = extract_text_from_pdf(input_file)

        if not file_contents.strip():
            st.error("PDF is empty. Please upload a valid PDF.")
            st.stop()
        prompt = f"""Summarize the following critique in a constructive way in
        1-Content Clarity
        2-Experience description
        3-Content Quality
        4-Content Originality
        5-improvements in the context of the {job_role} role: {file_contents}
        resume content {file_contents}"""

        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.completions.create(
            model="gpt-4o-mini",
            prompt=prompt,
            max_tokens=1000,
            temperature=0.7,
        )
        st.write(response.choices[0].text.strip())

    except Exception as e:
        st.error(f"An error occurred: {e}")