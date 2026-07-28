import tempfile

import pandas as pd

#from langchain.schema import Document
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader


def load_pdf(uploaded_file):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:

        tmp.write(uploaded_file.read())

        tmp_path = tmp.name

    loader = PyPDFLoader(tmp_path)

    documents = loader.load()

    return documents


def load_csv(uploaded_file):

    df = pd.read_csv(uploaded_file)

    text = df.to_string(index=False)

    return [Document(page_content=text)]


def load_document(uploaded_file):

    extension = uploaded_file.name.split(".")[-1].lower()

    if extension == "pdf":

        return load_pdf(uploaded_file)

    elif extension == "csv":

        return load_csv(uploaded_file)

    else:

        raise Exception("Formato no soportado.")
