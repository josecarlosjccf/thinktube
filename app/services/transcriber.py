import os
import whisper
import re

class AudioTranscriber:
    def __init__(self, output_dir="data/transcripts", model_size="base"):
        self.output_dir = output_dir
        self.model_size = model_size
        os.makedirs(self.output_dir, exist_ok=True)
        self.model = whisper.load_model(model_size)

    @staticmethod
    def format_transcript_text(text):
        """Formata o texto para melhor leitura."""
        text = re.sub(r'\s+', ' ', text).strip()
        text = re.sub(r'([.!?])\s+', r'\1\n\n', text)
        text = re.sub(r'([,])\s+([A-Z][a-z]+)', r'\1\n\2', text)
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text

    def transcribe_audio(self, audio_path: str) -> str:
        """Transcreve o áudio para texto e salva em um arquivo txt."""
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {audio_path}")
        base_name = os.path.splitext(os.path.basename(audio_path))[0]
        output_path = os.path.join(self.output_dir, f"{base_name}.txt")
        result = self.model.transcribe(audio_path)
        formatted_text = self.format_transcript_text(result["text"])
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(formatted_text)
        return output_path