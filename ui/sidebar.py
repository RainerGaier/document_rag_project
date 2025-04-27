import streamlit as st
from pathlib import Path

def show_sidebar():
    with st.sidebar:
        st.header("C O N T R O L &nbsp; P A N E L")

        with st.expander("F I L E &nbsp; U P L O A D I N G"):
            st.subheader("📂 Upload New Files")
            uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)
            if st.button("🗑️ Clear All Uploaded Files"):
                scratch_dir = Path("scratch")
                for file in scratch_dir.glob("*.pdf"):
                    file.unlink()
                st.success("All uploaded files cleared.")
            st.write("---")
 
            st.subheader("📄 Files to Include")
            scratch_dir = Path("scratch")
            scratch_files = list(scratch_dir.glob("*.pdf"))
            selected_files = {}
            for file in sorted(scratch_files):
                selected_files[file.name] = st.checkbox(file.name, value=True, key=file.name)

            ingest_button = st.button("🔄 Ingest All Uploaded Files")

        with st.expander("Q U E R Y &nbsp; M E"):
            st.subheader("🔍 Query Engine")
            query = st.text_input("Enter your search query")
            search_button = st.button("🔍 Search")

    return uploaded_files, selected_files, ingest_button, query, search_button