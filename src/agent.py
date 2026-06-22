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
    embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL_NAME)

    vector_store = Chroma(
        persist_directory=config.CHROMA_DB_DIR,
        embedding_function=embeddings,
    )

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 6,
            "fetch_k": 20,
            "lambda_mult": 0.7,
        },
    )

    llm = ChatCohere(model=config.COHERE_MODEL_NAME, temperature=config.TEMPERATURE)

    system_prompt = (
        "Você é o Assistente Inteligente do Campus. Sua função é responder dúvidas dos alunos "
        "com base exclusivamente nas fontes oficiais fornecidas no contexto abaixo.\n\n"
        "As fontes podem ser:\n"
        "  • Documentos PDF/DOCX/XLSX/TXT — identificados pelo caminho do arquivo no campo 'source'.\n"
        "  • Páginas web (URLs) — identificadas pela URL no campo 'source' e pelo campo 'title'.\n\n"
        "Regras obrigatórias:\n"
        "1. Responda APENAS com informações presentes no contexto fornecido. "
        "Nunca invente, deduza ou use conhecimento externo.\n"
        "2. Se a resposta não estiver no contexto, diga exatamente: "
        "\"Desculpe, mas não encontrei essa informação nas fontes oficiais do campus.\"\n"
        "3. Ao final de cada afirmação, cite a fonte entre colchetes:\n"
        "   - Para arquivos: [nome-do-arquivo]\n"
        "   - Para URLs: [Título da Página – https://...]\n"
        "4. Se a informação aparecer em mais de uma fonte, cite todas.\n\n"
        "Contexto das fontes:\n"
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, combine_docs_chain)

    return rag_chain