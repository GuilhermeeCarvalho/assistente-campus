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
            # Extrai o nome do arquivo dos metadados
            nome_arquivo = doc.metadata.get('source', 'Documento desconhecido')
            # Limpa o caminho completo para mostrar apenas o nome do arquivo
            nome_breve = nome_arquivo.split("\\")[-1].split("/")[-1]
            fontes_citadas.add(nome_breve)
            
        for fonte in fontes_citadas:
            print(f"- {fonte}")
        print("-" * 50)

if __name__ == "__main__":
    main()