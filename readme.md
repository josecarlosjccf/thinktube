
# ThinkTube



ThinkTube é um aplicativo colaborativo que gera resumos automáticos de vídeos do YouTube. Ele funciona baixando o áudio, transcrevendo o conteúdo e utilizando **modelos de linguagem open-source** para criar um resumo textual. Todo o fluxo é 100% gratuito e open-source, garantindo acessibilidade e praticidade.



---



## Como funciona?



-   Você insere o link de um vídeo do YouTube.

-   O sistema baixa o áudio do vídeo.

-   O áudio é transcrito automaticamente usando o modelo de IA **Whisper**.

-   A transcrição é resumida com modelos open-source (como BART ou Pegasus).

-   O resumo final é exibido na interface web.



---



## Estrutura do Projeto



```



thinktube/

├── app/

│   ├── main.py                  \# API principal (FastAPI)

│   └── services/

│       ├── downloader.py        \# Baixa áudio do YouTube

│       ├── transcriber.py       \# Transcreve o áudio

│       └── summarizer.py        \# Resume o texto

├── frontend/

│   ├── templates/

│   │   └── index.html           \# Página web principal

│   └── static/

│       └── style.css            \# Estilos CSS

├── data/

│   ├── downloads/               \# Áudios baixados

│   ├── transcripts/             \# Transcrições

│   └── summaries/               \# Resumos

├── requirements.txt             \# Dependências Python

├── README.md

└── .gitignore



````



---



## Como executar



### 1. Pré-requisitos



-   **Python 3.10+** (baixe [aqui](https://www.python.org/downloads/))

-   **ffmpeg** instalado.

    -   **Linux (Ubuntu/Debian):**

        ```

        sudo apt update && sudo apt install ffmpeg -y

        ```

    -   **Windows:** Baixe o [FFmpeg](https://ffmpeg.org/download.html), extraia-o e adicione a pasta `bin` ao PATH do sistema.



### 2. Configure o ambiente



1.  Crie e ative um ambiente virtual no terminal:

    ```

    python -m venv venv

    ```

2.  Ative o ambiente virtual:

    -   **Windows:**

        ```

        venv\Scripts\activate

        ```

    -   **Linux/Mac:**

        ```

        source venv/bin/activate

        ```

3.  Instale as dependências:

    ```

    pip install -r requirements.txt

    ```



### 3. Rode o ThinkTube



Execute o servidor com o comando abaixo. O servidor estará disponível em **http://localhost:8000**.



````



uvicorn app.main:app --reload



```



> **Aguarde o download dos modelos de IA no terminal.**



### 4. Como usar



1.  Acesse [http://localhost:8000](http://localhost:8000) no seu navegador.

2.  Cole a URL do vídeo do YouTube no campo e clique em "Resumir".

3.  Aguarde o processamento (o tempo pode variar dependendo do tamanho do vídeo). O resumo aparecerá na tela.



> **Observação:** Todos os arquivos de áudio, transcrições e resumos são salvos na pasta `data/` para acesso posterior.



---



## Solução de problemas



-   Verifique se o **ffmpeg** está instalado e adicionado ao seu PATH.

-   Para evitar o download repetido dos modelos, execute o projeto pelo menos uma vez com conexão à internet.

-   Se ocorrerem erros de dependência, certifique-se de que o ambiente virtual está ativado.



---



## Autores



**Ana Carla Xavier**



Responsável pelo download e transcrição do áudio.



[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AnaCarlaXO) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ana-carla-xavier-de-oliveira-945895366?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)



**José Carlos Candido**



Responsável pelo front-end e processamento da transcrição.



[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/josecarlosjccf) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jos%C3%A9-carlos-candido-73b723235?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

```
