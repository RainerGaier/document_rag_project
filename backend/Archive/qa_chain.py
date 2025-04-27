def build_qa_chain(retriever, llm):
    from langchain.chains import RetrievalQA

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain
