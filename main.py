from src.agent import inicializar_agente

def main():
    print("=== Inicializando o Assistente do Campus (Cohere) ===")
    agente = inicializar_agente()
    print("✅ Agente pronto para responder!")
    print("-" * 50)
    
    while True:
        pergunta = input("\nDigite sua pergunta (ou 'sair' para encerrar): ")
        if pergunta.lower() == 'sair':
            break
            
        if not pergunta.strip():
            continue
            
        print("🔍 Buscando nos documentos...")
        resposta = agente.invoke({"input": pergunta})
        
        print("\n🤖 Resposta do Agente:")
        print(resposta["answer"])
        
        print("\n📚 Fontes Utilizadas:")
        fontes_citadas = set()
        for doc in resposta["context"]:
            nome_arquivo = doc.metadata.get('source', 'Documento desconhecido')
            if isinstance(nome_arquivo, str) and nome_arquivo.startswith(("http://", "https://")):
                fontes_citadas.add(nome_arquivo)
            else:
                fontes_citadas.add(nome_arquivo.split("\\")[-1].split("/")[-1])
            
        for fonte in fontes_citadas:
            print(f"- {fonte}")
        print("-" * 50)

if __name__ == "__main__":
    main()