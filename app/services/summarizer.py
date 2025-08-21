import os
from transformers import pipeline

class TextSummarizer:
    def __init__(self, output_dir="data/summaries", model_name="facebook/bart-large-cnn"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.summarizer = pipeline("summarization", model=model_name)

    def summarize(self, transcript_path: str) -> str:
        """Gera resumo do texto transcrito e salva em arquivo txt."""
        if not os.path.exists(transcript_path):
            raise FileNotFoundError(f"Transcrição não encontrada: {transcript_path}")
        with open(transcript_path, encoding="utf-8") as f:
            text = f.read()
        # Limita o texto para não ultrapassar o tamanho do modelo (~1024 tokens)
        summary = self.summarizer(text[:2000], max_length=180, min_length=40, do_sample=False)[0]['summary_text']
        base_name = os.path.splitext(os.path.basename(transcript_path))[0]
        output_path = os.path.join(self.output_dir, f"{base_name}_summary.txt")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(summary)
        return output_path, summary