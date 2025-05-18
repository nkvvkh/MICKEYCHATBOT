import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# 🔐 Set your API key (not recommended for production)
os.environ["GOOGLE_API_KEY"] = "GOOGLE_API_KEY"

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Streamlit App UI
st.title("🤖 Gemini Chatbot")
st.markdown("Type a message and press Enter to chat with the AI. Type `quit` to stop.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]

# User input
user_input = st.text_input("You:", key="input")

# Process input
if user_input:
    if user_input.lower() == "quit":
        st.markdown("**Chat ended. Refresh to start again.**")
    else:
        st.session_state.chat_history.append(HumanMessage(content=user_input))
        try:
            result = llm.invoke(st.session_state.chat_history)
            st.session_state.chat_history.append(AIMessage(content=result.content))
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Display messages
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        st.markdown(f"**You:** {message.content}")
    elif isinstance(message, AIMessage):
        st.markdown(f"**AI:** {message.content}")import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# 🔐 Set your API key (not recommended for production)
os.environ["GOOGLE_API_KEY"] = "GOOGLE_API_KEY"

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Streamlit App UI
st.title("🤖 Gemini Chatbot")
st.markdown("Type a message and press Enter to chat with the AI. Type `quit` to stop.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]

# User input
user_input = st.text_input("You:", key="input")

# Process input
if user_input:
    if user_input.lower() == "quit":
        st.markdown("**Chat ended. Refresh to start again.**")
    else:
        st.session_state.chat_history.append(HumanMessage(content=user_input))
        try:
            result = llm.invoke(st.session_state.chat_history)
            st.session_state.chat_history.append(AIMessage(content=result.content))
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Display messages
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        st.markdown(f"**You:** {message.content}")
    elif isinstance(message, AIMessage):
        st.markdown(f"**AI:** {message.content}")
