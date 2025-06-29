# Transcrição de Vídeos do YouTube

Este projeto baixa vídeos do YouTube e transcreve o áudio usando Whisper.

## 📋 Pré-requisitos

1. **Python 3.7+**
2. **FFmpeg** (necessário para processamento de áudio)
3. **yt-dlp** (instalado via pip)

## 🛠️ Instalação

1. **Instalar dependências Python:**
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Instalar FFmpeg:**

   - 🐧 **Linux (Ubuntu/Debian)**
     ```bash
     sudo apt update && sudo apt install ffmpeg -y
     ```

   - 🪟 **Windows**
     - Baixe o FFmpeg do [site oficial](https://ffmpeg.org/)
     - Extraia o arquivo ZIP
     - Adicione a pasta `bin` ao PATH do sistema
     - Reinicie o terminal

## 🚀 Como Usar

### Executar o projeto:
```bash
cd src
python3 main.py
```

## 📁 Estrutura do Projeto

```
projeto/
├── src/
│   ├── main.py          # Script principal
│   ├── downloader.py    # Download de vídeos do YouTube
│   ├── transcriber.py   # Transcrição de áudio
│   ├── downloads/       # Arquivos de áudio baixados
│   └── transcripts/     # Transcrições geradas
├── .gitignore          # Arquivos ignorados pelo git
└── requirements.txt    # Dependências Python
```

## 🔧 Como Funciona

1. **Download**: O script baixa o áudio do vídeo do YouTube em formato MP3 usando yt-dlp via subprocess
2. **Transcrição**: Usa o modelo Whisper para transcrever o áudio para texto
3. **Saída**: Salva a transcrição em um arquivo .txt na pasta `transcripts/`

## 📝 Exemplo de Uso

```bash
$ cd src
$ python3 main.py
Cole a URL do YouTube: https://www.youtube.com/watch?v=exemplo
Baixando áudio...
Executando download...
Transcrevendo áudio...
Transcrição salva em: transcripts/nome_do_video.txt
```
