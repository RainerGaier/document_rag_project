from pathlib import Path
from docling.document_converter import DocumentConverter

doc_converter = DocumentConverter()


def extract_text_and_tables(file_path: Path):
    conversion_result = doc_converter.convert(file_path)

    texts = []
    tables = []

    for page in conversion_result.document.pages:
        texts.append({"text": page.text, "page_number": page.page_number})

    for idx, table in enumerate(conversion_result.document.tables):
        tables.append(
            {
                "table_text": table.to_text(),
                "page_number": table.page.page_number,
                "table_id": idx,
            }
        )

    return texts, tables
