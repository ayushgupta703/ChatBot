from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)

from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="AI Text Assistant", page_icon="")

st.title('AI Chatbot')
st.markdown("Hello! I'm your AI assistant. How can I assist you today?")

from google.oauth2.service_account import Credentials

def get_credentials():
    if "credentials" not in st.session_state:
        st.session_state["credentials"] = None
    
    credentials_path = os.getenv("GOOGLE_CREDENTIALS_PATH")
    
    if credentials_path:
        try:

            credentials = Credentials.from_service_account_file(credentials_path)
            st.session_state["credentials"] = credentials
        except FileNotFoundError:
            st.error("File not found. Please provide the correct path to your JSON file.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    
    return st.session_state["credentials"]

credentials = get_credentials()

if not credentials:
    st.warning("Please enter the path to your service account JSON file to continue.")
else:
    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(
                "You are a helpful AI assistant. Please respond to user queries in English."
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{question}"),
        ]
    )

    msgs = StreamlitChatMessageHistory(key="langchain_messages")

    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", credentials=credentials)

    chain = prompt | model | StrOutputParser()

    chain_with_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: msgs,
        input_messages_key="question",
        history_messages_key="chat_history",
    )

    user_input = st.text_input("Enter your question in English:", "")

    if user_input:
        st.chat_message("human").write(user_input)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            config = {"configurable": {"session_id": "any"}}

            response = chain_with_history.stream({"question": user_input}, config)

            for res in response:
                full_response += res or ""
                message_placeholder.markdown(full_response + "|")
                message_placeholder.markdown(full_response)
