import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Add it in .env file.")

# Free local embedding model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Groq LLM model
LLM_MODEL = "llama-3.1-8b-instant"

# Chunk settings
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Number of chunks to retrieve
TOP_K = 5

# FAISS path
VECTORSTORE_PATH = "vectorstore/faiss_index"