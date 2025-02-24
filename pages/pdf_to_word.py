import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
import io

st.title("PDF to Word")
st.write("This application converts PDF to Word")

uploaded_file = st.file_uploader("Upload your PDF here:", type=["pdf"])

if uploaded_file is not None:
    pdf_file = PdfReader(uploaded_file)
    st.write("PDF file uploaded successfully")

    num_pages = len(pdf_file.pages)
    st.write("Number of pages: ", num_pages)

    doc = Document()

    for i in range(num_pages):
        page = pdf_file.pages[i]
        text = page.extract_text()
        doc.add_paragraph(text)

    word_io = io.BytesIO()
    doc.save(word_io)   
    word_io.seek(0)

    st.download_button(
        label="Download Word file", 
        data=word_io.getvalue(), 
        file_name="Converted.docx", 
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
