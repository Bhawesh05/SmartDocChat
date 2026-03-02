# ============================================================
# SmartDocChat - AI-Powered Document Q&A Application
# Author: Bhawesh Patankar
# GitHub: https://github.com/Bhawesh05
# ============================================================

import streamlit as st
from src.doc_handler import handle_uploaded_file
from src.chat_engine import get_chat_response, clear_memory
from src.ui_components import render_sidebar, render_header, render_chat_message

# --- Page Configuration ---
st.set_page_config(
    page_title="SmartDocChat | Bhawesh Patankar",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Session State Init ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "doc_name" not in st.session_state:
    st.session_state.doc_name = None

# --- Header ---
render_header()

# --- Sidebar ---
uploaded_file, openai_api_key = render_sidebar()

# --- Process uploaded document ---
if uploaded_file and openai_api_key:
    if st.session_state.doc_name != uploaded_file.name:
        with st.spinner("📄 Processing your document..."):
            vector_store = handle_uploaded_file(uploaded_file, openai_api_key)
            if vector_store:
                st.session_state.vector_store = vector_store
                st.session_state.doc_name = uploaded_file.name
                st.session_state.chat_history = []
                st.success(f"✅ **{uploaded_file.name}** loaded successfully!")
            else:
                st.error("❌ Could not process this file. Please try again.")

# --- Chat Interface ---
st.markdown("---")

if st.session_state.vector_store is None:
    st.markdown(
        """
        <div style='text-align:center; padding: 60px 0; color: #888;'>
            <h2>👆 Upload a document from the sidebar to get started</h2>
            <p>Supports PDF, CSV, and TXT files</p>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    # Display chat history
    for message in st.session_state.chat_history:
        render_chat_message(message["role"], message["content"])

    # Chat input
    user_input = st.chat_input("Ask anything about your document...")

    if user_input:
        # Show user message
        render_chat_message("user", user_input)
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # Get AI response
        with st.spinner("🧠 Thinking..."):
            response = get_chat_response(
                user_input,
                st.session_state.vector_store,
                st.session_state.chat_history,
                openai_api_key
            )

        # Show assistant response
        render_chat_message("assistant", response)
        st.session_state.chat_history.append({"role": "assistant", "content": response})

    # Clear chat button
    if st.session_state.chat_history:
        if st.button("🗑️ Clear Chat", key="clear_chat"):
            st.session_state.chat_history = []
            clear_memory()
            st.rerun()
