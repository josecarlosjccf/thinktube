import os
import whisper
import re

def format_transcript_text(text):

    # Remove espaços extras
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Adiciona quebras de linha após pontuação
    text = re.sub(r'([.!?])\s+', r'\1\n\n', text)
    
    # Adiciona quebras de linha após vírgulas em frases longas
    text = re.sub(r'([,])\s+([A-Z][a-z]+)', r'\1\n\2', text)
    
    # Remove quebras de linha duplas excessivas
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    return text

def transcribe_audio(
    input_path: str,
    output_dir: str = None,
    model_size: str = "base"
) -> str:
    # Define o diretório transcripts dentro de src
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(__file__), 'transcripts')
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {input_path}")
    
    model = whisper.load_model(model_size)

    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(output_dir, f"{base_name}.txt")
    
    result = model.transcribe(input_path)
    
    # Formata o texto para melhor legibilidade
    formatted_text = format_transcript_text(result["text"])
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return output_path