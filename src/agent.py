from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate

try:
    from langchain.chains import create_retrieval_chain
    from langchain.chains.combine_documents import create_stuff_documents_chain
except ImportError:
    from langchain_classic.chains import create_retrieval_chain
    from langchain_classic.chains.combine_documents import create_stuff_documents_chain

from src import config


def inicializar_agente():
    # 1. Carregar o mesmo modelo de embedding usado na ingestão
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # 2. Conectar ao banco de dados Chroma existente
    vector_store = Chroma(
        persist_directory=config.CHROMA_DB_DIR, 
        embedding_function=embeddings
    )
    
    # 3. Configurar o buscador (Retriever) para trazer os 3 trechos mais relevantes
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    
    # 4. Inicializar a LLM da Cohere
    llm = ChatCohere(model=config.COHERE_MODEL_NAME, temperature=config.TEMPERATURE)
    
    # 5. Criar o Prompt Rígido Anti-Alucinação
    system_prompt = (
        "Você é o Assistente Inteligente do Campus. Sua tarefa é responder às dúvidas dos alunos "
        "com base estritamente nos documentos oficiais fornecidos no contexto.\n\n"
        "Regras Críticas:\n"
        "1. Responda APENAS com base nas informações do contexto fornecido.\n"
        "2. Se a informação não estiver expressamente escrita no contexto, responda exatamente: "
        "\"Desculpe, mas não encontrei essa informação nos documentos oficiais do campus.\""
        "Não tente inventar, deduzir ou usar conhecimentos externos.\n"
        "3. Para cada afirmação que fizer, cite o nome do arquivo fonte encontrado nos metadados.\n\n"
        "Contexto de documentos:\n"
        "{context}"
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])
    
    # 6. Criar as correntes de execução (Chains)
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, combine_docs_chain)
    
    return rag_chain