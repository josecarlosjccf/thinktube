# ThinkTube

ThinkTube é uma aplicação colaborativa que permite gerar resumos automáticos de vídeos do YouTube. O sistema baixa o áudio do vídeo, transcreve o conteúdo falado e utiliza modelos de linguagem de código aberto para criar um resumo textual. Todo o fluxo é realizado com tecnologias gratuitas e open source, proporcionando praticidade e acessibilidade.

## ✨ O que o ThinkTube faz?
- O usuário insere o link de um vídeo do YouTube.
- O sistema faz o download do áudio do vídeo.
- O áudio é transcrito automaticamente usando o modelo Whisper.
- O texto transcrito é resumido utilizando modelos open source (como BART ou Pegasus).
- O resumo é exibido de forma simples pelo frontend web.

## 📁 Estrutura de Pastas

```
thinktube/
├── app/
│   ├── main.py                  # Inicialização da API FastAPI e integração dos serviços
│   └── services/
│       ├── downloader.py        # Classe para download de áudio do YouTube
│       ├── transcriber.py       # Classe para transcrição de áudio
│       └── summarizer.py        # Classe para sumarização de texto
├── frontend/
│   ├── templates/
│   │   └── index.html           # Página HTML principal
│   └── static/
│       └── style.css            # Estilos CSS
├── data/
│   ├── downloads/               # Áudios baixados
│   ├── transcripts/             # Transcrições geradas
│   └── summaries/               # Resumos gerados
├── requirements.txt             # Dependências Python do projeto
├── README.md
└── .gitignore
```

## 🚀 Como rodar o projeto

### 1. Pré-requisitos

- Python 3.10+ instalado ([baixe aqui](https://www.python.org/downloads/))
- ffmpeg instalado no sistema:
  - **Linux (Ubuntu/Debian):**
    ```bash
    sudo apt update && sudo apt install ffmpeg -y
    ```
  - **Windows:**  
    Baixe o [FFmpeg](https://ffmpeg.org/download.html), extraia e adicione a pasta `bin` ao PATH do sistema.

### 2. Crie e ative um ambiente virtual

No terminal, execute:

```bash
python -m venv venv
```

- Ative o ambiente:
  - **Windows:**
    ```bash
    venv\Scripts\activate
    ```
  - **Linux/Mac:**
    ```bash
    source venv/bin/activate
    ```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o ThinkTube (frontend + backend)

No terminal, rode:

```bash
uvicorn app.main:app --reload
```
### AGUARDE O MODELO DE IA SER BAIXADO NO TERMINAL

O servidor estará disponível em [http://localhost:8000](http://localhost:8000).

### 5. Como usar

1. Acesse [http://localhost:8000](http://localhost:8000) no seu navegador.
2. Cole a URL de um vídeo do YouTube no campo indicado.
3. Clique em "Resumir".
4. Aguarde alguns minutos (o tempo depende do tamanho do vídeo); o resumo aparecerá na tela.

> **Observação:**  
> - O processamento pode demorar para vídeos longos.  
> - Todos os áudios, transcrições e resumos são salvos na pasta `data/` para consulta posterior.

## 🛠️ Dicas de uso e solução de problemas

- Certifique-se de que o ffmpeg está instalado e disponível no PATH.
- Para não baixar novamente o modelo do Whisper ou do HuggingFace, recomenda-se rodar pelo menos uma vez com internet disponível.
- Se aparecer erro de dependência, verifique se está no ambiente virtual correto.

## 👥 Autores

(em breve)