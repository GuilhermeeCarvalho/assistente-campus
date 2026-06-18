import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
DATA_URLS_FILE = os.path.join(BASE_DIR, "data", "urls.txt")
CHROMA_DB_DIR = os.path.join(BASE_DIR, "data", "chroma_db")

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
EMBEDDING_MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
COHERE_MODEL_NAME = "command-a-03-2025"
TEMPERATURE = 0.0

COHERE_API_KEY = os.getenv("COHERE_API_KEY")

if not COHERE_API_KEY:
    raise ValueError("ERRO: defina COHERE_API_KEY no arquivo .env")