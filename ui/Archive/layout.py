import streamlit as st

def display_chunks(chunks, metadatas):
    st.subheader("🔎 Extracted Chunks")
    for idx, (chunk, metadata) in enumerate(zip(chunks, metadatas)):
        with st.expander(f"Chunk {idx+1} - {metadata.get('type', 'text')} (Page {metadata.get('page_number', '?')})"):
            st.write(chunk)