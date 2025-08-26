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
│       ├── transcriber.py       # Transcrição de áudio (Whisper)
│       └── summarizer.py        # Resumo de texto (BART/Pegasus)
├── data/
│   ├── audio/                   # Áudios baixados
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
    <li><b>Linux (Ubuntu/Debian):</b><br><code>sudo apt update && sudo apt install ffmpeg -y</code></li>
    <li><b>Windows:</b> Baixe o <a href="https://ffmpeg.org/download.html">FFmpeg</a>, extraia e adicione a pasta <code>bin</code> ao PATH do sistema.</li>
  </ul>
</ul>

<h3>2. Crie e ative um ambiente virtual</h3>
<pre><code>python -m venv venv</code></pre>
<p><b>Windows:</b> <code>venv\Scripts\activate</code><br>
<b>Linux/Mac:</b> <code>source venv/bin/activate</code></p>

<h3>3. Instale as dependências</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>4. Execute o ThinkTube</h3>
<pre><code>uvicorn app.main:app --reload</code></pre>

<p>Servidor disponível em <a href="http://localhost:8000">http://localhost:8000</a></p>

<h3>5. Como usar</h3>
<ol>
  <li>Acesse <a href="http://localhost:8000">http://localhost:8000</a></li>
  <li>Cole a URL de um vídeo do YouTube</li>
  <li>Clique em "Resumir"</li>
  <li>O resumo aparecerá na tela após o processamento</li>
</ol>

<blockquote>
  <b>Observação:</b><br>
  • O processamento pode ser demorado para vídeos longos.<br>
  • Todos os áudios, transcrições e resumos ficam na pasta <code>data/</code>.
</blockquote>

<hr>

<h2>🛠️ Dicas de uso</h2>
<ul>
  <li>Certifique-se de que o ffmpeg está instalado e no PATH.</li>
  <li>Para não baixar os modelos novamente, rode pelo menos uma vez com internet.</li>
  <li>Se houver erro de dependência, confira se está no ambiente virtual correto.</li>
</ul>

<hr>

<h2>👥 Autores</h2>

<p><b>Ana Carla Xavier</b><br>
Responsável pelo download e transcrição de áudio.<br>
<a href="https://github.com/AnaCarlaXO"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
<a href="https://www.linkedin.com/in/ana-carla-xavier-de-oliveira-945895366?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
</p>

<p><b>José Carlos Candido</b><br>
Responsável pelo front-end e processamento da transcrição.<br>
<a href="https://github.com/josecarlosjccf"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
<a href="https://www.linkedin.com/in/jos%C3%A9-carlos-candido-73b723235?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
</p>
