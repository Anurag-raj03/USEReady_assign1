import streamlit as st
import requests
API_URL = "http://backend:8000/extract"
st.title("Rental Agreement Metadata Extractor")
uploaded_file = st.file_uploader(
    "Upload Rental Agreement (.docx, .png, .jpg)",
    type=["docx", "png", "jpg", "jpeg"]
)
if uploaded_file is not None:
    if st.button("Extract Metadata"):
        with st.spinner("Processing..."):
            files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
            response = requests.post(API_URL, files=files)
            if response.status_code == 200:
                st.success("Extraction Complete")
                st.json(response.json())
            else:
                st.error("Extraction Failed")
                st.write(response.text)