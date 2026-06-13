from pathlib import Path

from .config import CHROMA_DB_DIR, RAW_DIR


def ingest_pdfs(raw_dir: Path = RAW_DIR, db_dir: Path = CHROMA_DB_DIR) -> None:
    """Placeholder for PDF ingestion and chunking into ChromaDB."""
    db_dir.mkdir(parents=True, exist_ok=True)
    raw_dir.mkdir(parents=True, exist_ok=True)
    print(f"Prepared ingestion from {raw_dir} to {db_dir}")


if __name__ == "__main__":
    ingest_pdfs()
