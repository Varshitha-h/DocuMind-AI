import os

from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()


class Settings:
    """
    Application configuration loaded from environment variables.
    """

    APP_NAME = os.getenv(
        "APP_NAME",
        "DocuMind AI"
    )

    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "all-MiniLM-L6-v2"
    )

    LLM_MODEL = os.getenv(
        "LLM_MODEL",
        "llama3.2"
    )
    OLLAMA_API_KEY = os.getenv(
        "OLLAMA_API_KEY",
        ""
    )


    TOP_K = int(
        os.getenv(
            "TOP_K",
            3
        )
    )

    UPLOAD_DIR = os.getenv(
        "UPLOAD_DIR",
        "uploads"
    )


settings = Settings()