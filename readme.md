# Resumidor de Vídeos do YouTube via Link

Projeto colaborativo com o objetivo de desenvolver uma aplicação capaz de gerar resumos automáticos a partir de vídeos do YouTube. O sistema utilizará ferramentas gratuitas para transcrição e modelos de linguagem open source para geração de resumo.

---

## 🎯 Objetivo

Permitir que o usuário insira o link de um vídeo do YouTube e receba um **resumo automático** do conteúdo falado, usando apenas ferramentas e modelos gratuitos.

---

## 🧰 Tecnologias Utilizadas

### Backend (principal)
- **Python 3.10+**
- **FastAPI** – criação de API leve e eficiente
- **yt-dlp** – download do áudio do vídeo do YouTube
- **Whisper** (via Hugging Face ou `whisper.cpp`) – transcrição de áudio
- **Transformers da Hugging Face** – geração de resumo com modelos gratuitos como:
  - `facebook/bart-large-cnn`
  - `google/pegasus-cnn_dailymail`
  - `philschmid/bart-large-cnn-samsum`

### Frontend (opcional)
- **JavaScript, HTML e CSS**
- Ou **Gradio** (caso prefiram uma interface rápida em Python)

---

## ⚙️ Funcionalidades Esperadas

1. Inserção de link de vídeo do YouTube
2. Extração e transcrição do áudio
3. Geração de resumo textual
4. Exibição ou retorno do resumo ao usuário (via terminal, API ou interface web)

---

## 📦 Estrutura Sugerida do Projeto

```
.
├── app/
│   ├── main.py              # API principal com FastAPI
│   ├── transcriber.py       # Lógica de transcrição (Whisper)
│   ├── summarizer.py        # Lógica de resumo (Transformers)
│   └── utils.py             # Funções auxiliares
├── frontend/ (opcional)     # Interface web simples
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 👥 Divisão de Responsabilidades

As tarefas serão divididas em três grandes áreas:

1. **Processamento de Vídeo e Transcrição**  
   - Extração do áudio via `yt-dlp`  
   - Transcrição com Whisper (`whisper.cpp` ou Hugging Face)

2. **Geração de Resumo com Modelos Open Source**  
   - Processamento de texto transcrito  
   - Aplicação de modelos como BART, Pegasus ou T5

3. **API e Interface (opcional)**  
   - Criação da API com FastAPI  
   - Interface simples com Gradio ou HTML/JS

---

## ⏳ Prazo Máximo de Entrega

**22 de julho de 2025**  
A ideia é ter um sistema funcional até essa data, com tempo para testes e melhorias, se necessário.

---

## 💡 Melhorias Futuras (se houver tempo)

- Exportar resumos em PDF/TXT
- Suporte a múltiplos idiomas
- Geração de resumos em tópicos ou bullet points
- Armazenamento em banco de dados local

