def answer_question(question: str) -> str:
    """Placeholder for the RAG agent logic."""
    question = question.strip()
    if not question:
        return "Digite uma pergunta para iniciar."
    return (
        "Ainda estou sem a base de documentos carregada. "
        f"Pergunta recebida: {question}"
    )
