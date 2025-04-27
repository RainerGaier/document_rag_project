from pathlib import Path
import fitz  # PyMuPDF

def extract_text_and_tables(file_path: Path):
    doc = fitz.open(file_path)

    texts = []
    tables = []  # No table support for now; can add if you want later.

    for page in doc:
        page_text = page.get_text("text")
        if page_text.strip():
            texts.append({
                "text": page_text,
                "page_number": page.number + 1
            })

    return texts, tables