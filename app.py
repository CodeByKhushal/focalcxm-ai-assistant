import os
import base64
import re
import html
import streamlit as st

from rag_pipeline import get_answer


st.set_page_config(
    page_title="FocalCXM AI Assistant",
    page_icon="🤖",
    layout="centered"
)


def format_answer(text):
    text = html.escape(text)
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
    text = text.replace("\n", "<br>")
    return text


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Montserrat', sans-serif;
}

.stApp {
    background-color: #F7F7F7;
}

.header-wrapper {
    display: flex;
    align-items: center;
    gap: 22px;
    margin-bottom: 20px;
    flex-wrap: wrap;
}

.logo-img {
    width: 150px;
    max-width: 100%;
}

.header-text {
    flex: 1;
    min-width: 260px;
}

.main-title {
    color: #002856;
    font-size: 42px;
    font-weight: 700;
    line-height: 1.1;
    margin-bottom: 8px;
}

.subtitle {
    color: #555555;
    font-size: 18px;
    font-weight: 600;
}

label {
    font-weight: 600 !important;
    color: #002856 !important;
}

.stTextInput input {
    border: 2px solid #0598CE;
    border-radius: 10px;
    padding: 10px;
}

.stButton > button {
    background-color: #002856;
    color: white;
    border-radius: 10px;
    padding: 10px 22px;
    border: none;
    font-weight: 700;
}

.response-card {
    background-color: #E3EDFD;
    border-left: 6px solid #0598CE;
    border-radius: 14px;
    padding: 24px;
    margin-top: 25px;
    box-shadow: 0 4px 14px rgba(0, 40, 86, 0.12);
    color: #000000;
    font-size: 16px;
    line-height: 1.7;
}

.response-title {
    color: #002856;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 14px;
}

.suggested {
    color: #1E4278;
    font-weight: 700;
    font-size: 22px;
}
</style>
""", unsafe_allow_html=True)


logo_path = "assets/FocalCXMLogo1.png"
logo_html = "🤖"

if os.path.exists(logo_path):
    with open(logo_path, "rb") as image_file:
        encoded_logo = base64.b64encode(image_file.read()).decode()
    logo_html = f'<img src="data:image/png;base64,{encoded_logo}" class="logo-img">'


st.markdown(f"""
<div class="header-wrapper">
    <div>{logo_html}</div>
    <div class="header-text">
        <div class="main-title">FocalCXM AI Assistant</div>
        <div class="subtitle">
            AI-powered assistant for FocalCXM knowledge and services.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


st.markdown("---")

query = st.text_input("Enter your question:")

if st.button("Ask") and query:
    with st.spinner("Thinking..."):
        answer = get_answer(query)
        formatted_answer = format_answer(answer)

    st.markdown(f"""
    <div class="response-card">
        <div class="response-title">🤖 AI Response</div>
        {formatted_answer}
    </div>
    """, unsafe_allow_html=True)


st.markdown("---")

st.markdown(
    '<div class="suggested">Suggested Questions</div>',
    unsafe_allow_html=True
)

st.markdown("""
- What services does FocalCXM offer?
- What is CRM Blueprinting?
- What Veeva services does FocalCXM provide?
- What industries does FocalCXM support?
- What resources are available on the website?
""")