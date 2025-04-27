from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

def chunk_texts(text_items):
    chunks = []
    metadatas = []

    for item in text_items:
        split_chunks = splitter.split_text(item["text"])
        for chunk in split_chunks:
            chunks.append(chunk)
            metadatas.append({
                "type": "text",
                "page_number": item["page_number"]
            })

    return chunks, metadatas

def chunk_tables(table_items):
    chunks = []
    metadatas = []

    for table in table_items:
        split_chunks = splitter.split_text(table["table_text"])
        for chunk in split_chunks:
            chunks.append(chunk)
            metadatas.append({
                "type": "table",
                "page_number": table["page_number"],
                "table_id": table["table_id"]
            })

    return chunks, metadatas