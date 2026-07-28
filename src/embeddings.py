from langchain_openai import OpenAIEmbeddings


def create_embeddings():
    """
    Crea el modelo de embeddings.
    """
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    return embeddings
