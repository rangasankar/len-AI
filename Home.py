import streamlit as st

st.set_page_config(
    page_title="Langchain Chatbot",
    page_icon='💬',
    layout='wide'
)

st.write("""
[
![Visitors](https://raw.githubusercontent.com/rangasankar/len-AI/main/len.jpg)
""")
st.header("Lenovo IntelliStore LLM AI Advisor")
st.write("""
Langchain is a powerful framework designed to streamline the development of applications using Language Models (LLMs). IntelliStore Advisor leverages the power of Langchain and AI Large Language models to search the internet, search standalone documents and provide answers for Storage related questions.

- **Basic StorageBot**: Engage in interactive conversations with the LLM about Storage.
- **Storagebot with Internet Access**: An internet-enabled chatbot capable of answering user queries using internet.
- **StorageBot with Lenovo documents** Empower the chatbot with the ability to access custom Lenovo documents, enabling it to provide answers to user queries based on the referenced information.

To explore sample usage of each Storagebot, please navigate to the corresponding chatbot section.
""")