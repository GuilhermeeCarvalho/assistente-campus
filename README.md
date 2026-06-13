# assistente-campus

Assistente universitario com RAG (Retrieval-Augmented Generation) para responder perguntas com base em documentos PDF oficiais do campus.

## Pre-requisitos

- Python 3.10+ instalado
- Git instalado
- Conta na Cohere com chave de API valida

## Estrutura esperada do projeto

```text
assistente-campus/
├── data/
│   ├── raw/          # PDFs oficiais usados como base
│   └── chroma_db/    # Indice vetorial gerado pela ingestao
├── src/
│   ├── config.py
│   ├── ingestion.py
│   └── agent.py
├── main.py
├── requirements.txt
└── .env
```

## Passo a passo completo (do zero)

### 1. Clonar o repositorio

```bash
git clone <URL_DO_REPOSITORIO>
cd assistente-campus
```

### 2. Criar e ativar ambiente virtual (venv)

Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Windows (Git Bash):

```bash
python -m venv venv
source venv/Scripts/activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Criar arquivo .env com a chave da Cohere

O projeto usa Cohere para gerar respostas. O arquivo `.env` deve existir na raiz com a variavel abaixo:

```env
COHERE_API_KEY=sua_chave_api_aqui
```

Sem essa variavel o projeto nao inicializa.

### 5. Colocar os PDFs de referencia

Copie os documentos PDF oficiais para:

```text
data/raw/
```

### 6. Gerar o indice vetorial (ingestao)

Com a venv ativa, execute:

```bash
python -m src.ingestion
```

Esse comando:

- le os PDFs em `data/raw/`
- divide em chunks
- gera embeddings
- salva o banco vetorial em `data/chroma_db/`

### 7. Executar o assistente

```bash
python main.py
```

No terminal, digite suas perguntas. Para sair:

```text
sair
```

## Fluxo para atualizar documentos

Sempre que adicionar/remover PDFs em `data/raw/`, rode novamente:

```bash
python -m src.ingestion
```

Depois execute o bot novamente com `python main.py`.

## Solucao de problemas rapida

- Erro de chave ausente:
	Verifique se existe `.env` na raiz com `COHERE_API_KEY`.
- Bot responde "nao encontrei essa informacao":
	Verifique se os PDFs estao em `data/raw/` e rode `python -m src.ingestion`.
- Erro de modulo nao encontrado:
	Confirme se a venv esta ativa e se `pip install -r requirements.txt` foi executado nela.
