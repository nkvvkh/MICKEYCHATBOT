import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# --- Sidebar ---
st.sidebar.title("⚙️ Settings")
api_key = st.sidebar.text_input("🔑 Google API Key", type="password", key="api_key_input")

if not api_key:
    st.warning("Please enter your Google API key in the sidebar.")
    st.stop()

if st.sidebar.button("🧹 Reset Chat"):
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]
    st.rerun()

# --- LLM Setup ---
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key="AIzaSyB9M5GA9fiH_lXQGhxvx4CWwkLHXdiNZ1U"
)

# --- Initialize chat history ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]

# --- Main Chat UI ---
st.title("🤖 Gemini Chatbot")

# Show previous chat
for message in st.session_state.chat_history:
    with st.chat_message("user" if isinstance(message, HumanMessage) else "ai"):
        st.markdown(message.content)

# --- Input box ---
user_input = st.chat_input("Type your message here...")

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    # Get response
    try:
        response = llm.invoke(st.session_state.chat_history)
        st.session_state.chat_history.append(AIMessage(content=response.content))

        # Display response
        with st.chat_message("ai"):
            st.markdown(response.content)

    except Exception as e:
        st.error(f"❌ Something went wrong: {str(e)}")
