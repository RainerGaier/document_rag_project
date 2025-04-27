from langchain.vectorstores import Milvus
from langchain.embeddings import HuggingFaceEmbeddings

embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vector_store = Milvus(
    embedding_function=embedding_function,
    collection_name="docling_rag",
    connection_args={"host": "localhost", "port": "19530"},
)


def store_chunks(chunks, metadatas):
    vector_store.add_texts(chunks, metadatas)


def get_retriever():
    return vector_store.as_retriever()
