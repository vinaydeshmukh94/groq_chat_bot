import streamlit as st
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import json

load_dotenv()

model_name = "llama-3.3-70b-versatile"

groq_key = os.getenv("GROQ_API_KEY")

st.title("Langchain chat usgin GROQ")

groq_chat = ChatGroq(
    api_key=groq_key,
    model_name = model_name,
    temperature=0.9,
    max_tokens=100
)

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Display chat history
for chat in st.session_state['chat_history']:
    with st.chat_message(chat['role']):
        st.write(chat['content'])

prompt = st.chat_input("Enter your message here")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state['chat_history'].append({"role": "user", "content": prompt})

    with st.spinner("Loading..."):
        response = groq_chat.invoke(prompt)
        response = json.loads(response.json())
        response_content = response['content']

        with st.chat_message("assistant"):
            st.write(response_content)

        st.session_state['chat_history'].append({"role": "assistant", "content": response_content})