<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ThinkTube</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        body {
            font-family: 'Roboto', sans-serif;
            line-height: 1.6;
            color: #333;
            margin: 0;
            padding: 20px;
            background-color: #f4f7f9;
        }
        .container {
            max-width: 900px;
            margin: auto;
            background: #fff;
            padding: 30px 40px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            color: #1a2a4b;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 10px;
            margin-top: 30px;
        }
        h1 {
            text-align: center;
            font-size: 2.5em;
        }
        h2 {
            font-size: 1.8em;
        }
        p {
            margin-bottom: 20px;
            text-align: justify;
        }
        ul, ol {
            margin-bottom: 20px;
            padding-left: 20px;
        }
        li {
            margin-bottom: 10px;
        }
        a {
            color: #0077b5;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
        .code-block {
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
            font-family: 'Courier New', Courier, monospace;
        }
        .info-box {
            background-color: #e6f7ff;
            border-left: 5px solid #0077b5;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
        .button-group {
            display: flex;
            gap: 10px;
            align-items: center;
        }
        .button-group img {
            height: 24px;
            width: 24px;
        }
        .button {
            display: flex;
            align-items: center;
            padding: 8px 16px;
            border-radius: 5px;
            font-weight: bold;
            color: white;
            text-decoration: none;
            transition: transform 0.2s ease-in-out;
        }
        .button:hover {
            transform: translateY(-2px);
            text-decoration: none;
        }
        .github-button {
            background-color: #333;
        }
        .linkedin-button {
            background-color: #0077b5;
        }
        .author {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

<div class="container">

    <h1>ThinkTube</h1>
    <p>ThinkTube é um aplicativo colaborativo que gera resumos automáticos de vídeos do YouTube. Ele funciona baixando o áudio, transcrevendo o conteúdo e utilizando <strong>modelos de linguagem open-source</strong> para criar um resumo textual. Todo o fluxo é 100% gratuito e open-source, garantindo acessibilidade e praticidade.</p>

    <hr>

    <h2>Como funciona?</h2>
    <ul>
        <li>Você insere o link de um vídeo do YouTube.</li>
        <li>O sistema baixa o áudio do vídeo.</li>
        <li>O áudio é transcrito automaticamente usando o modelo de IA **Whisper**.</li>
        <li>A transcrição é resumida com modelos open-source (como BART ou Pegasus).</li>
        <li>O resumo final é exibido na interface web.</li>
    </ul>

    <hr>

    <h2>Estrutura do Projeto</h2>
    <div class="code-block">
        <pre><code>thinktube/
├── app/
│   ├── main.py                  # API principal (FastAPI)
│   └── services/
│       ├── downloader.py        # Baixa áudio do YouTube
│       ├── transcriber.py       # Transcreve o áudio
│       └── summarizer.py        # Resume o texto
├── frontend/
│   ├── templates/
│   │   └── index.html           # Página web principal
│   └── static/
│       └── style.css            # Estilos CSS
├── data/
│   ├── downloads/               # Áudios baixados
│   ├── transcripts/             # Transcrições
│   └── summaries/               # Resumos
├── requirements.txt             # Dependências Python
├── README.md
└── .gitignore</code></pre>
    </div>

    <hr>

    <h2>Como executar</h2>
    <h3>1. Pré-requisitos</h3>
    <ul>
        <li><strong>Python 3.10+</strong> (baixe <a href="https://www.python.org/downloads/">aqui</a>)</li>
        <li><strong>ffmpeg</strong> instalado.
            <ul>
                <li><strong>Linux (Ubuntu/Debian):</strong>
                    <div class="code-block">
                        <pre><code>sudo apt update && sudo apt install ffmpeg -y</code></pre>
                    </div>
                </li>
                <li><strong>Windows:</strong> Baixe o <a href="https://ffmpeg.org/download.html">FFmpeg</a>, extraia-o e adicione a pasta `bin` ao PATH do sistema.</li>
            </ul>
        </li>
    </ul>

    <h3>2. Configure o ambiente</h3>
    <p>1. Crie e ative um ambiente virtual no terminal:</p>
    <div class="code-block">
        <pre><code>python -m venv venv</code></pre>
    </div>
    <p>2. Ative o ambiente virtual:</p>
    <ul>
        <li><strong>Windows:</strong>
            <div class="code-block">
                <pre><code>venv\Scripts\activate</code></pre>
            </div>
        </li>
        <li><strong>Linux/Mac:</strong>
            <div class="code-block">
                <pre><code>source venv/bin/activate</code></pre>
            </div>
        </li>
    </ul>
    <p>3. Instale as dependências:</p>
    <div class="code-block">
        <pre><code>pip install -r requirements.txt</code></pre>
    </div>

    <h3>3. Rode o ThinkTube</h3>
    <p>Execute o servidor com o comando abaixo. O servidor estará disponível em <strong>http://localhost:8000</strong>.</p>
    <div class="code-block">
        <pre><code>uvicorn app.main:app --reload</code></pre>
    </div>
    <div class="info-box">
        <p>Aguarde o download dos modelos de IA no terminal.</p>
    </div>

    <h3>4. Como usar</h3>
    <ol>
        <li>Acesse <a href="http://localhost:8000">http://localhost:8000</a> no seu navegador.</li>
        <li>Cole a URL do vídeo do YouTube no campo e clique em "Resumir".</li>
        <li>Aguarde o processamento (o tempo pode variar dependendo do tamanho do vídeo). O resumo aparecerá na tela.</li>
    </ol>
    <div class="info-box">
        <p><strong>Observação:</strong> Todos os arquivos de áudio, transcrições e resumos são salvos na pasta <code>data/</code> para acesso posterior.</p>
    </div>

    <hr>

    <h2>Solução de problemas</h2>
    <ul>
        <li>Verifique se o **ffmpeg** está instalado e adicionado ao seu PATH.</li>
        <li>Para evitar o download repetido dos modelos, execute o projeto pelo menos uma vez com conexão à internet.</li>
        <li>Se ocorrerem erros de dependência, certifique-se de que o ambiente virtual está ativado.</li>
    </ul>

    <hr>

    <h2>Autores</h2>
    <div class="author">
        <h3>Ana Carla Xavier</h3>
        <p>Responsável pelo download e transcrição do áudio.</p>
        <div class="button-group">
            <a href="https://github.com/AnaCarlaXO" class="button github-button">
                <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Logo"> GitHub
            </a>
            <a href="https://www.linkedin.com/in/ana-carla-xavier-de-oliveira-945895366?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" class="button linkedin-button">
                <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Logo"> LinkedIn
            </a>
        </div>
    </div>
    <div class="author">
        <h3>José Carlos Candido</h3>
        <p>Responsável pelo front-end e processamento da transcrição.</p>
        <div class="button-group">
            <a href="https://github.com/josecarlosjccf" class="button github-button">
                <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Logo"> GitHub
            </a>
            <a href="https://www.linkedin.com/in/jos%C3%A9-carlos-candido-73b723235?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" class="button linkedin-button">
                <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Logo"> LinkedIn
            </a>
        </div>
    </div>

</div>

</body>
</html>
