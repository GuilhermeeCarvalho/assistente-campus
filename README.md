# assistente-campus

Assistente universitario com RAG (Retrieval-Augmented Generation) para responder perguntas com base em documentos oficiais do campus em diferentes formatos.

## Pre-requisitos

- Python 3.10+ instalado
- Git instalado
- Conta na Cohere com chave de API valida

## Estrutura esperada do projeto

```text
assistente-campus/
├── data/
│   ├── raw/          # Arquivos oficiais usados como base
│   ├── urls.txt      # Lista opcional de URLs, uma por linha
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

### 5. Colocar os documentos de referencia

Copie os documentos oficiais para:

```text
data/raw/
```

Formatos aceitos dentro de `data/raw/`:

- `pdf`
- `txt`
- `docx`
- `csv`
- `xlsx`
- `.url` com uma URL por arquivo

Para ingerir páginas web, crie também o arquivo opcional:

```text
data/urls.txt
```

e coloque uma URL por linha.

### 6. Gerar o indice vetorial (ingestao)

Com a venv ativa, execute:

```bash
python -m src.ingestion
```

Este comando:

- le os arquivos suportados em `data/raw/`
- le URLs em `data/urls.txt`, se o arquivo existir
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

Sempre que adicionar/remover arquivos em `data/raw/` ou URLs em `data/urls.txt`, rode novamente:

```bash
python -m src.ingestion
```

Depois execute o bot novamente com `python main.py`.

## Solucao de problemas rapida

- Erro de chave ausente:
	Verifique se existe `.env` na raiz com `COHERE_API_KEY`.
- Bot responde "nao encontrei essa informacao":
	Verifique se os documentos estao em `data/raw/` ou em `data/urls.txt` e rode `python -m src.ingestion`.
- Erro de modulo nao encontrado:
	Confirme se a venv esta ativa e se `pip install -r requirements.txt` foi executado nela.
