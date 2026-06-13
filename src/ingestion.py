import os
import shutil
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from src import config

def executar_ingestao():
    print("🔄 Iniciando o processo de ingestão de documentos...")
    
    # 1. Validar se a pasta raw contém arquivos
    if not os.path.exists(config.DATA_RAW_DIR) or not os.listdir(config.DATA_RAW_DIR):
        print(f"❌ Erro: A pasta '{config.DATA_RAW_DIR}' está vazia ou não existe.")
        return

    # 2. Carregar todos os PDFs da pasta configurada
    print(f"📂 Lendo PDFs de: {config.DATA_RAW_DIR}")
    loader = PyPDFDirectoryLoader(config.DATA_RAW_DIR)
    documentos = loader.load()
    print(f"📄 Total de páginas carregadas: {len(documentos)}")

    # 3. Fragmentação Inteligente (Chunking)
    print("✂️ Dividindo os documentos em blocos de texto (chunks)...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
        add_start_index=True  # Rastreia a posição exata do bloco no documento
    )
    chunks = text_splitter.split_documents(documentos)
    print(f"🧩 Total de chunks gerados: {len(chunks)}")

    # 4. Inicializar o mesmo modelo de embedding usado na consulta
    print("🧠 Gerando embeddings e configurando o banco de dados...")
    embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL_NAME)

    # 5. Criar e Persistir o Banco de Vetores (ChromaDB)
    # O Chroma lê o diretório configurado; se não existir, ele cria automaticamente
    if os.path.exists(config.CHROMA_DB_DIR):
        print(f"🧹 Limpando índice anterior em: {config.CHROMA_DB_DIR}")
        shutil.rmtree(config.CHROMA_DB_DIR)
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=config.CHROMA_DB_DIR
    )
    
    print(f"✅ Ingestão concluída com sucesso! Banco salvo em: {config.CHROMA_DB_DIR}")

if __name__ == "__main__":
    executar_ingestao()