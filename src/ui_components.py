# ============================================================
# SmartDocChat - UI Components Module
# Author: Bhawesh Patankar
# GitHub: https://github.com/Bhawesh05
# Handles: All Streamlit UI rendering functions
# ============================================================

import streamlit as st


def render_header():
    """Renders the main app header."""
    st.markdown(
        """
        <div style='text-align:center; padding: 20px 0 10px 0;'>
            <h1 style='color:#4F8BF9;'>🧠 SmartDocChat</h1>
            <p style='color:#888; font-size:16px;'>
                Chat with your documents using AI — by 
                <a href='https://github.com/Bhawesh05' target='_blank' style='color:#4F8BF9;'>
                    Bhawesh Patankar
                </a>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_sidebar():
    """
    Renders the sidebar with file upload and API key input.

    Returns:
        tuple: (uploaded_file, openai_api_key)
    """
    with st.sidebar:
        st.image(
            "https://img.shields.io/badge/SmartDocChat-Bhawesh05-4F8BF9?style=for-the-badge&logo=github",
            use_column_width=True
        )
        st.markdown("## ⚙️ Setup")

        # OpenAI API Key
        openai_api_key = st.text_input(
            "🔑 OpenAI API Key",
            type="password",
            placeholder="sk-...",
            help="Get your API key from https://platform.openai.com/api-keys"
        )

        st.markdown("---")
        st.markdown("## 📄 Upload Document")

        uploaded_file = st.file_uploader(
            "Choose a file",
            type=["pdf", "csv", "txt"],
            help="Supported: PDF, CSV, TXT"
        )

        st.markdown("---")
        st.markdown(
            """
            ### 💡 How to Use
            1. Enter your OpenAI API key
            2. Upload a PDF, CSV, or TXT file
            3. Ask any question about the document
            4. SmartDocChat remembers your conversation!
            """)

        st.markdown("---")
        st.markdown(
            """
            <div style='text-align:center; font-size:12px; color:#888;'>
                Built with ❤️ by <b>Bhawesh Patankar</b><br>
                <a href='https://github.com/Bhawesh05/SmartDocChat' target='_blank'>
                    GitHub: Bhawesh05
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    return uploaded_file, openai_api_key


def render_chat_message(role: str, content: str):
    """
    Renders a single chat message with custom styling.

    Args:
        role (str): 'user' or 'assistant'
        content (str): Message text
    """
    if role == "user":
        with st.chat_message("user", avatar="👤"):
            st.markdown(content)
    else:
        with st.chat_message("assistant", avatar="🧠"):
            st.markdown(content)
