import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-5")

st.set_page_config(
    page_title="Flight Operations Assistant",
    page_icon="✈️",
    layout="centered",
)

st.title("✈️ Flight Operations Assistant")
st.write(
    "An AI learning assistant for students exploring "
    "aircraft and aerospace engineering."
)

st.info(
    "Educational tool only — not a replacement for official "
    "aviation procedures or professional guidance."
)

if not API_KEY:
    st.error("OPENAI_API_KEY is missing. Please add it to your .env file.")
    st.stop()

client = OpenAI(api_key=API_KEY)

SYSTEM_PROMPT = """
You are an educational aerospace assistant for students.

Explain basic concepts related to:
- aircraft components
- lift, drag, thrust and weight
- flight controls
- aircraft stability
- basic aircraft performance
- runway and flight-operation concepts
- aerospace engineering

Use simple, beginner-friendly explanations.

For questions involving real-world aviation operations or
safety-critical decisions, clearly state that the answer is
educational and that actual aviation decisions must follow
official procedures and qualified professionals.

Do not invent aircraft-specific procedures, regulations,
limits, or performance values.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


def ask_assistant(question):
    response = client.responses.create(
        model=MODEL,
        instructions=SYSTEM_PROMPT,
        input=
