import os

from dotenv import load_dotenv


def load_environment():
    """
    Carga las variables del archivo .env
    """

    load_dotenv()

    return {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")
    }
