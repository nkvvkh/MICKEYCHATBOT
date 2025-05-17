import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# 🔐 Set your API key
os.environ["GOOGLE_API_KEY"] = "GOOGLE_API_KEY"  # Replace with your actual API key

# 🤖 Initialize the Gemini model (Gemini 1.5 Flash is fast & efficient)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# 🧠 Initialize chat history in Streamlit session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]

# 📌 Streamlit app title
st.title("💬 Chat with Gemini 1.5 Flash")
st.markdown("Ask me anything!")

# 🗨️ Display chat history
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("ai").write(msg.content)

# 📝 User input
if prompt := st.chat_input("Type your message..."):
    # Show user message
    st.chat_message("user").write(prompt)
    st.session_state.chat_history.append(HumanMessage(content=prompt))

    try:
        # Get Gemini response
        response = llm.invoke(st.session_state.chat_history)
        st.chat_message("ai").write(response.content)
        st.session_state.chat_history.append(AIMessage(content=response.content))
    except Exception as e:
        st.error(f"❌ Error: {e}")

