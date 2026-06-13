import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Caminhos de Pastas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
CHROMA_DB_DIR = os.path.join(BASE_DIR, "data", "chroma_db")

# Configurações do RAG
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
MODEL_NAME = "gpt-4o-mini"  # Rápido, barato e excelente para seguir regras estritas
TEMPERATURE = 0.0           # Zero garante respostas determinísticas (anti-alucinação)

# Validação simples
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("ERRO: OPENAI_API_KEY não foi encontrada no arquivo .env")