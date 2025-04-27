import streamlit as st
from pathlib import Path

from backend.document_loader import extract_text_and_tables
from backend.chunker import chunk_texts, chunk_tables
from backend.vector_store import store_chunks, load_vectorstore, get_retriever
from backend.llm_model import llm
from backend.qa_chain import build_qa_chain
from ui.sidebar import show_sidebar
from ui.layout import display_chunks

st.set_page_config(page_title="DOCUMENT SEARCH", page_icon="📄", layout="wide")

# Show initializing message
st.info("🛠️ Initializing the system ... Please wait.")
st.info("✅ Initialized")
st.title("📄🔍 DOCUMENT Search Application")

uploaded_files, selected_files, ingest_clicked, query, search_clicked = show_sidebar()

# Handle uploaded files
if uploaded_files:
    scratch_dir = Path("scratch")
    scratch_dir.mkdir(parents=True, exist_ok=True)
    for uploaded_file in uploaded_files:
        temp_path = scratch_dir / uploaded_file.name
        temp_path.write_bytes(uploaded_file.read())

# Handle ingestion
if ingest_clicked:
    scratch_dir = Path("scratch")
    files_to_ingest = [fname for fname, selected in selected_files.items() if selected]
    all_chunks = []
    all_metadatas = []
    if files_to_ingest:
        with st.spinner("Ingesting selected files..."):
            for file_name in files_to_ingest:
                file_path = scratch_dir / file_name
                texts, tables = extract_text_and_tables(file_path)
                text_chunks, text_meta = chunk_texts(texts)
                table_chunks, table_meta = chunk_tables(tables)
                # Inject filename into metadata
                for meta in text_meta + table_meta:
                    meta["source"] = file_name  # <-- Add filename to every metadata entry
                combined_chunks = text_chunks + table_chunks
                combined_metadatas = text_meta + table_meta

                if combined_chunks:
                    all_chunks.extend(combined_chunks)
                    all_metadatas.extend(combined_metadatas)
        if all_chunks:
            store_chunks(all_chunks, all_metadatas)
            st.success("✅ Ingest completed and vectorstore saved.")

# Always try loading vectorstore
vector_store_loaded = load_vectorstore()

# Search query handling
if search_clicked and query and vector_store_loaded:
    retriever = get_retriever()
    qa_chain = build_qa_chain(retriever, llm)

    with st.spinner("Generating answer..."):
        result = qa_chain.invoke({"query": query})
        st.subheader("📢 Answer")
        st.write(result['result'])
        st.subheader("📚 Source Documents")
        with st.expander("S O U R C E &nbsp; D E T A I L S"):
            for doc in result['source_documents']:
                st.markdown(f"**Source:** {doc.metadata.get('source', 'Unknown')}")
                st.markdown(f"**Page:** {doc.metadata.get('page_number', 'Unknown')}")
                st.markdown(f"**Type:** {doc.metadata.get('type', 'Unknown')}")
                st.write(doc.page_content)
                st.markdown("---")