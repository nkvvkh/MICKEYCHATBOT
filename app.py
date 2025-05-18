import os
os.environ["GOOGLE_API_KEY"] = "GOOGLE_API_KEY"
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Sidebar for API key input
st.sidebar.title("🔐 Gemini Settings")
api_key = st.sidebar.text_input("Enter your Google API Key", type="password")

# Prevent execution without API key
if not api_key:
    st.warning("Please enter your Google API key in the sidebar to continue.")
    st.stop()

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)

# App title
st.title("🤖 Gemini Chatbot")
st.markdown("Chat with the AI below. Type 'quit' or 'exit' to end the conversation.")

# Initialize session chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]

# Display previous messages
for message in st.session_state.chat_history:
    with st.chat_message("user" if isinstance(message, HumanMessage) else "ai"):
        st.markdown(message.content)

# Input box
user_input = st.chat_input("Type your message here...")

# Handle user input
if user_input:
    if user_input.lower() in ["quit", "exit"]:
        st.session_state.chat_history.append(HumanMessage(content=user_input))
        with st.chat_message("user"):
            st.markdown(user_input)
        with st.chat_message("ai"):
            st.markdown("👋 Goodbye! Refresh to restart.")
    else:
        # Append user message
        st.session_state.chat_history.append(HumanMessage(content=user_input))
        with st.chat_message("user"):
            st.markdown(user_input)

        # Get AI response
        try:
            result = llm.invoke(st.session_state.chat_history)
            st.session_state.chat_history.append(AIMessage(content=result.content))
            with st.chat_message("ai"):
                st.markdown(result.content)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")


