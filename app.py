import streamlit as st

from src.utils import load_environment

load_environment()

from src.loader import load_document
from src.splitter import split_document
from src.embeddings import create_embeddings
from src.vectorstore import create_vectorstore
from src.agent import create_qa_chain

"""
import streamlit as st

from src.loader import load_document
from src.splitter import split_document
from src.embeddings import create_embeddings
from src.vectorstore import create_vectorstore
from src.agent import create_qa_chain
"""

st.set_page_config(
    page_title="Challenge Agente IA",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Agente Inteligente RAG")

st.write(
    """
    Carga un archivo PDF o CSV y realiza preguntas sobre su contenido.
    """
)

uploaded_file = st.file_uploader(
    "Selecciona un PDF o CSV",
    type=["pdf", "csv"]
)

if uploaded_file:

    with st.spinner("Procesando documento..."):

        documents = load_document(uploaded_file)

        chunks = split_document(documents)

        embeddings = create_embeddings()

        vectorstore = create_vectorstore(chunks, embeddings)

        qa_chain = create_qa_chain(vectorstore)

    st.success("Documento procesado correctamente.")

    question = st.text_input("Haz una pregunta")

    if question:

        with st.spinner("Generando respuesta..."):

            response = qa_chain.invoke(question)

        st.subheader("Respuesta")

        st.write(response)

else:

    st.info("Carga un documento para comenzar.")
