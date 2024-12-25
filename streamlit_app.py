# Code refactored from https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps

from openai import OpenAI
import streamlit as st

# Streamlit app title
st.title('Ericsson EOC Quotation Creation Bot')
# Set your OpenAI API key (you can also set it in environment variables for security)
client = OpenAI(
    api_key=st.secrets['general']['OPENAI_API_KEY'],  # This is the default and can be omitted
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o",
)