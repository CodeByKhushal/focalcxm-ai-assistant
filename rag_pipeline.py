from groq import Groq

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

import config


embeddings = HuggingFaceEmbeddings(
    model_name=config.EMBEDDING_MODEL
)


vector_store = FAISS.load_local(
    config.VECTORSTORE_PATH,
    embeddings,
    allow_dangerous_deserialization=True,
)


retriever = vector_store.as_retriever(
    search_kwargs={"k": config.TOP_K}
)


client = Groq(
    api_key=config.GROQ_API_KEY
)


def get_answer(query):
    docs = retriever.get_relevant_documents(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a professional AI assistant for FocalCXM.

Use the provided context to answer questions about FocalCXM services, solutions, business areas, technologies, and company information.

If partial information exists, summarize it professionally instead of saying no information exists.

Keep the answer complete and concise. Do not start a numbered point unless you can finish it.

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model=config.LLM_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful company website assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1.0,
        max_tokens=300,
    )

    return response.choices[0].message.content