from src.agent import inicializar_agente

def main():
    print("=== Inicializando o Assistente do Campus (Cohere) ===")
    agente = inicializar_agente()
    print("Agente pronto para responder!")
    print("-" * 50)
    
    while True:
        pergunta = input("\nDigite sua pergunta (ou 'sair' para encerrar): ")
        if pergunta.lower() == 'sair':
            break
            
        if not pergunta.strip():
            continue
            
        print("Buscando nos documentos...")
        try:
            resposta = agente.invoke({"input": pergunta})
            
            print("\nResposta do Agente:")
            print(resposta.get("answer", "Sem resposta."))
            
            print("\nFontes Utilizadas:")
            fontes_citadas = set()
            for doc in resposta.get("context", []):
                nome_arquivo = doc.metadata.get('source', 'Documento desconhecido')
                if isinstance(nome_arquivo, str) and nome_arquivo.startswith(("http://", "https://")):
                    fontes_citadas.add(nome_arquivo)
                else:
                    fontes_citadas.add(nome_arquivo.split("\\")[-1].split("/")[-1])
                
            for fonte in fontes_citadas:
                print(f"- {fonte}")
        except Exception as e:
            print("\nOcorreu um erro de conexão ou de processamento.")
            print(f"Detalhes: {e}")
            print("Verifique sua internet ou a chave da API e tente novamente.")
            
        print("-" * 50)

if __name__ == "__main__":
    main()