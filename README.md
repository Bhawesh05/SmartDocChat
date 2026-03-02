# 🧠 SmartDocChat

### An AI-powered document Q&A assistant with conversational memory — chat with your CSV, PDF, and TXT files naturally. 📄

> Built by **Bhawesh Patankar** | [GitHub: Bhawesh05](https://github.com/Bhawesh05)

---

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-0.1.16-green?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-orange?style=for-the-badge&logo=openai)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## 📌 What is SmartDocChat?

**SmartDocChat** is an AI-powered conversational assistant that lets you **upload any document** and ask questions about it in plain English. Powered by **LangChain + OpenAI**, it uses vector embeddings and retrieval-augmented generation (RAG) to give accurate, context-aware answers — and remembers your conversation history so follow-up questions work naturally.

---

## ✨ Features

- 💬 **Conversational Memory** — remembers previous questions for natural dialogue
- 📄 **Multi-format Support** — works with PDF, CSV, and TXT files
- 🔍 **FAISS Vector Search** — fast similarity search over your document
- 🧠 **RAG Architecture** — answers grounded strictly in your document
- 🚀 **Streamlit UI** — clean, responsive web interface
- ☁️ **Deployment Ready** — Procfile included for Heroku/cloud deployment

---

## 🗂️ Project Structure

```
SmartDocChat/
│
├── home.py                  # Main Streamlit application entry point
│
├── src/
│   ├── __init__.py          # Package init
│   ├── doc_handler.py       # File loading, text splitting, embedding
│   ├── chat_engine.py       # LangChain conversational chain + memory
│   └── ui_components.py     # Streamlit UI rendering functions
│
├── embeddings/              # FAISS vector index (generated at runtime)
│   └── .gitkeep
│
├── requirements.txt         # Python dependencies
├── setup.sh                 # Streamlit server config script
├── Procfile                 # Cloud deployment config
├── .env.example             # Example environment variables
├── .gitignore
├── .gitattributes
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Git
- OpenAI API Key ([get one here](https://platform.openai.com/api-keys))

### Installation

**1. Clone the repository:**
```bash
git clone https://github.com/Bhawesh05/SmartDocChat.git
cd SmartDocChat
```

**2. Create a virtual environment:**
```bash
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run the app:**
```bash
streamlit run home.py
```

**5. Open in your browser:** `http://localhost:8501`

---

## 🔑 Usage

1. Enter your **OpenAI API Key** in the sidebar
2. **Upload** a PDF, CSV, or TXT file
3. **Ask questions** about your document in plain English
4. SmartDocChat will answer based on the document content
5. Ask **follow-up questions** — it remembers the conversation!

---

## 🛠️ Tech Stack

| Technology | Role |
|---|---|
| **Python 3.8+** | Core language |
| **LangChain** | Conversational AI chain orchestration |
| **OpenAI GPT-3.5** | Language model |
| **FAISS** | Vector similarity search |
| **Streamlit** | Web application UI |
| **PyPDF** | PDF parsing |

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

**Contact:** [GitHub: Bhawesh05](https://github.com/Bhawesh05)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  Built with ❤️ by <b>Bhawesh Patankar</b> | <a href="https://github.com/Bhawesh05">@Bhawesh05</a>
</div>
