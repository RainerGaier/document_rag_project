from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path

VECTORSTORE_DIR = Path("scratch/vectorstore/")
VECTORSTORE_DIR.mkdir(parents=True, exist_ok=True)
EMBEDDINGS_MODEL_NAME = "all-MiniLM-L6-v2"

_embeddings = HuggingFaceEmbeddings(model_name=EMBEDDINGS_MODEL_NAME)
_vector_store = None

def store_chunks(chunks, metadatas):
    global _vector_store
    _vector_store = FAISS.from_texts(chunks, _embeddings, metadatas=metadatas)
    _vector_store.save_local(VECTORSTORE_DIR.as_posix())

def load_vectorstore():
    global _vector_store
    if (VECTORSTORE_DIR / "index.faiss").exists():
        _vector_store = FAISS.load_local(
            VECTORSTORE_DIR.as_posix(), _embeddings, allow_dangerous_deserialization=True
        )
    return _vector_store

def get_retriever():
    return _vector_store.as_retriever() if _vector_store else None