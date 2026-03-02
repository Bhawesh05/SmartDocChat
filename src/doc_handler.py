# ============================================================
# SmartDocChat - Document Handler Module
# Author: Bhawesh Patankar
# GitHub: https://github.com/Bhawesh05
# Handles: PDF, CSV, TXT file reading and vector embedding
# ============================================================

import os
import tempfile
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, CSVLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings


def handle_uploaded_file(uploaded_file, openai_api_key: str):
    """
    Reads the uploaded file, splits text into chunks,
    and creates a FAISS vector store.

    Args:
        uploaded_file: Streamlit UploadedFile object
        openai_api_key (str): OpenAI API key for embeddings

    Returns:
        FAISS vector store or None on failure
    """
    try:
        file_ext = os.path.splitext(uploaded_file.name)[1].lower()

        with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        # Load document based on file type
        if file_ext == ".pdf":
            loader = PyPDFLoader(tmp_path)
        elif file_ext == ".csv":
            loader = CSVLoader(tmp_path)
        elif file_ext == ".txt":
            loader = TextLoader(tmp_path, encoding="utf-8")
        else:
            st.error(f"Unsupported file type: {file_ext}")
            return None

        documents = loader.load()

        # Split into chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = splitter.split_documents(documents)

        # Create embeddings and vector store
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        vector_store = FAISS.from_documents(chunks, embeddings)

        # Save locally in embeddings folder
        vector_store.save_local("embeddings/faiss_index")

        os.unlink(tmp_path)
        return vector_store

    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None
