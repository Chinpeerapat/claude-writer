import os
import streamlit as st
from dotenv import load_dotenv
from anthropic import Anthropic

client = Anthropic(
    # This is the default and can be omitted
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)
    
# with st.sidebar:
#     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("Claude Extension")

uploaded_file = st.file_uploader("Upload an article", type=("txt", "md"))

question = st.text_input(
    "Ask anything",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)

if uploaded_file and question and not api_key:
    st.info("Please add your Anthropic API key to continue.")

if uploaded_file and question and api_key:
    article = uploaded_file.read().decode()
    prompt = f"""{anthropic.HUMAN_PROMPT} Here's an article:\n\n
    {article}\n\n\n\n{question}{anthropic.AI_PROMPT}"""

    response = client.completions.create(
        prompt=prompt,
        stop_sequences=[anthropic.HUMAN_PROMPT],
        model="claude-3-opus-20240229",
        max_tokens_to_sample=4000,
    )
    st.write("### Answer")
    st.write(response.completion)
