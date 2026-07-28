from langchain_community.vectorstores import FAISS


def create_vectorstore(chunks, embeddings):
    """
    Crea la base vectorial FAISS.
    """

    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vectorstore
