import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# 🔑 Set your API key
os.environ["GOOGLE_API_KEY"] = "GOOGLE_API_KEY"  # Replace with your actual key

# 🤖 Initialize the model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")  # or "gemini-1.5-pro"

# 🧠 Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]

# 🖼️ App Title
st.title("💬 Gemini Chatbot with LangChain")

# 📝 Display past chat messages
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("ai").write(msg.content)

# 💬 Input field
if prompt := st.chat_input("Type your message here..."):
    # Add user message
    st.session_state.chat_history.append(HumanMessage(content=prompt))
    st.chat_message("user").write(prompt)

    # Get AI response
    try:
        response = llm.invoke(st.session_state.chat_history)
        st.session_state.chat_history.append(AIMessage(content=response.content))
        st.chat_message("ai").write(response.content)
    except Exception as e:
        st.error(f"An error occurred: {e}")
