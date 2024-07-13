import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini Pro API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to interact with Gemini Pro model
def get_gemini_response(text, jd):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_prompt.format(text=text, jd=jd))
    return response.text

# Function to extract text from uploaded PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfFileReader(uploaded_file)
    text = ""
    for page in range(reader.numPages):
        page_obj = reader.getPage(page)
        text += page_obj.extract_text()
    return text

# Prompt Template
input_prompt = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response as per below structure
{{"JD Match": "%", "MissingKeywords": [], "Profile Summary": ""}}
"""

# Streamlit app layout
st.sidebar.title("Smart ATS for Resumes")
st.sidebar.subheader("About")
st.sidebar.write("This sophisticated ATS project, developed with Gemini Pro and Streamlit, seamlessly incorporates advanced features including resume match percentage, keyword analysis to identify missing criteria, and the generation of comprehensive profile summaries, enhancing the efficiency and precision of the candidate evaluation process for discerning talent acquisition professionals.")

st.sidebar.markdown("""
- [Streamlit](https://streamlit.io/)
- [Gemini Pro](https://deepmind.google/technologies/gemini/#introduction)
- [makersuit API Key](https://makersuite.google.com/)
- [Github Repository](https://github.com/praj2408/End-To-End-Resume-ATS-Tracking-LLM-Project-With-Google-Gemini-Pro)
""")

add_vertical_space(5)

st.title("Smart Application Tracking System")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None and jd:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(text, jd)
        st.subheader(response)
    else:
        st.warning("Please upload a PDF file and enter a job description to proceed.")
