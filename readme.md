<h1>ThinkTube</h1>
<p>ThinkTube é uma aplicação colaborativa que permite gerar resumos automáticos de vídeos do YouTube. O sistema baixa o áudio do vídeo, transcreve o conteúdo falado e utiliza modelos de linguagem de código aberto para criar um resumo textual. Todo o fluxo é realizado com tecnologias gratuitas e open source, proporcionando praticidade e acessibilidade.</p>
<hr>
<h2>✨ O que o ThinkTube faz?</h2>
<ul>
    <li>O usuário insere o link de um vídeo do YouTube.</li>
    <li>O sistema faz o download do áudio do vídeo.</li>
    <li>O áudio é transcrito automaticamente usando o modelo Whisper.</li>
    <li>O texto transcrito é resumido utilizando modelos open source (como BART ou Pegasus).</li>
    <li>O resumo é exibido de forma simples pelo frontend web.</li>
</ul>
<hr>
<h2>📁 Estrutura de Pastas</h2>
<pre><code>thinktube/
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
└── .gitignore</code></pre>
<hr>
<h2>🚀 Como rodar o projeto</h2>
<h3>1. Pré-requisitos</h3>
<ul>
    <li>Python 3.10+ instalado (<a href="https://www.python.org/downloads/">baixe aqui</a>)</li>
    <li>ffmpeg instalado no sistema:</li>
    <ul>
        <li><strong>Linux (Ubuntu/Debian):</strong>
            <pre><code>sudo apt update && sudo apt install ffmpeg -y</code></pre>
        </li>
        <li><strong>Windows:</strong> Baixe o <a href="https://ffmpeg.org/download.html">FFmpeg</a>, extraia e adicione a pasta <code>bin</code> ao PATH do sistema.</li>
    </ul>
</ul>
<h3>2. Crie e ative um ambiente virtual</h3>
<p>No terminal, execute:</p>
<pre><code>python -m venv venv</code></pre>
<p>Ative o ambiente:</p>
<ul>
    <li><strong>Windows:</strong>
        <pre><code>venv\Scripts\activate</code></pre>
    </li>
    <li><strong>Linux/Mac:</strong>
        <pre><code>source venv/bin/activate</code></pre>
    </li>
</ul>
<h3>3. Instale as dependências</h3>
<pre><code>pip install -r requirements.txt</code></pre>
<h3>4. Execute o ThinkTube (frontend + backend)</h3>
<p>No terminal, rode:</p>
<pre><code>uvicorn app.main:app --reload</code></pre>
<h3>AGUARDE O MODELO DE IA SER BAIXADO NO TERMINAL</h3>
<p>O servidor estará disponível em <a href="http://localhost:8000">http://localhost:8000</a>.</p>
<h3>5. Como usar</h3>
<ol>
    <li>Acesse <a href="http://localhost:8000">http://localhost:8000</a> no seu navegador.</li>
    <li>Cole a URL de um vídeo do YouTube no campo indicado.</li>
    <li>Clique em "Resumir".</li>
    <li>Aguarde alguns minutos (o tempo depende do tamanho do vídeo); o resumo aparecerá na tela.</li>
</ol>
<blockquote><strong>Observação:</strong>
<ul>
    <li>O processamento pode demorar para vídeos longos.</li>
    <li>Todos os áudios, transcrições e resumos são salvos na pasta <code>data/</code> para consulta posterior.</li>
</ul>
</blockquote>
<hr>
<h2>🛠️ Dicas de uso e solução de problemas</h2>
<ul>
    <li>Certifique-se de que o ffmpeg está instalado e disponível no PATH.</li>
    <li>Para não baixar novamente o modelo do Whisper ou do HuggingFace, recomenda-se rodar pelo menos uma vez com internet disponível.</li>
    <li>Se aparecer erro de dependência, verifique se está no ambiente virtual correto.</li>
</ul>
<hr>
<h2>👥 Autores</h2>
<p><strong>Ana Carla Xavier</strong>: Responsável pelo download do áudio do vídeo e a transcrição do áudio.<br>
<a href="https://github.com/AnaCarlaXO"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Botão GitHub"></a></p>
<p><strong>José Carlos Candido</strong>: Responsável pelo front end e processamento da transcrição.<br>
<a href="https://github.com/josecarlosjccf"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Botão GitHub"></a></p>
