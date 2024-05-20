import pathlib
import textwrap
import streamlit as st
from PIL import Image

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


st.title('Gemini Pro Vision Demo')

genai.configure(api_key=st.secrets["api_key"])
model = genai.GenerativeModel('gemini-pro-vision')

uploaded_file = st.file_uploader(
    "Upload a .jpg image", type=["jpg", "png", "jpeg"])
uploaded_text = st.text_area("Enter your query here.")

if st.button("Ask Gemini"):
    if uploaded_file is not None:
        img = Image.open(uploaded_file)

        response = model.generate_content(["Give a discription of the image",img])
        st.write(to_markdown(response.text).data)

    if uploaded_text and uploaded_file is not None:
        response = model.generate_content([uploaded_text, img])
        st.write(to_markdown(response.text).data)
