from langchain.chains import RetrievalQA

from langchain_openai import ChatOpenAI


def create_qa_chain(vectorstore):
    """
    Construye la cadena RAG.
    """

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k": 4
        }
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )

    return qa_chain
