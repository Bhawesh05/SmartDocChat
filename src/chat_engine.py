# ============================================================
# SmartDocChat - Chat Engine Module
# Author: Bhawesh Patankar
# GitHub: https://github.com/Bhawesh05
# Handles: LangChain conversational chain with memory
# ============================================================

from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

# Global memory object (persists during session)
_memory = None


def _get_memory():
    """Returns or initialises the conversation memory."""
    global _memory
    if _memory is None:
        _memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )
    return _memory


def clear_memory():
    """Resets conversation memory."""
    global _memory
    _memory = None


def get_chat_response(
    user_question: str,
    vector_store,
    chat_history: list,
    openai_api_key: str
) -> str:
    """
    Generates an AI response using LangChain ConversationalRetrievalChain.

    Args:
        user_question (str): The user's input question
        vector_store: FAISS vector store with document embeddings
        chat_history (list): List of previous messages
        openai_api_key (str): OpenAI API key

    Returns:
        str: AI-generated answer
    """
    try:
        llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.2,
            openai_api_key=openai_api_key
        )

        retriever = vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 4}
        )

        memory = _get_memory()

        # Custom prompt to keep answers grounded in the document
        qa_prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""
You are SmartDocChat, an intelligent AI assistant created by Bhawesh Patankar.
Your job is to answer questions ONLY based on the provided document context.
If the answer is not in the context, say: "I couldn't find that in the document."

Context:
{context}

Question: {question}

Answer:"""
        )

        chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=retriever,
            memory=memory,
            return_source_documents=False,
            combine_docs_chain_kwargs={"prompt": qa_prompt}
        )

        result = chain({"question": user_question})
        return result.get("answer", "Sorry, I could not generate a response.")

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
