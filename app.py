import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from prompt_templates import get_chat_prompt
from chat_history import ChatHistory

# Load API key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Set Streamlit config
st.set_page_config(page_title="SmartBro Chat", page_icon="🤖")
st.title("🤖 SmartBro Chat - Powered by LangChain + Groq")

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = ChatHistory()
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    model_choice = st.selectbox("Choose Model", ["llama3-8b-8192", "mixtral-8x7b-32768"])
    temperature = st.slider("Temperature", 0.0, 1.5, 0.7, 0.1)
    if st.button("🔄 Clear Chat"):
        st.session_state.chat_history.clear()
        st.session_state.chat_log = []
        st.experimental_rerun()

# Input box
user_input = st.chat_input("Type your message...")

# Init LLM
llm = ChatGroq(
    model_name=model_choice,
    temperature=temperature
)

# Get prompt
prompt = get_chat_prompt()

# Handle user input
if user_input:
    st.session_state.chat_history.add_user_message(user_input)
    formatted_messages = prompt.format_messages(
        chat_history=st.session_state.chat_history.get(),
        user_input=user_input
    )
    response = llm.invoke(formatted_messages)
    st.session_state.chat_history.add_ai_message(response.content)
    st.session_state.chat_log.append(("user", user_input))
    st.session_state.chat_log.append(("ai", response.content))

# Display chat
for role, message in st.session_state.chat_log:
    if role == "user":
        with st.chat_message("user"):
            st.markdown(message)
    else:
        with st.chat_message("ai"):
            st.markdown(message)
