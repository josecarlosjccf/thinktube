import os
import re
from typing import List, Tuple, Optional
from transformers import pipeline
import logging

class TextSummarizer:
    def __init__(
        self,
        output_dir: str = "data/summaries",
        model_name: str = "facebook/bart-large-cnn"
    ):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.model_name = model_name
        self.summarizer = self._load_summarizer()
        self.token_limit = self._get_token_limit()
        logging.basicConfig(level=logging.INFO)

    def _load_summarizer(self):
        try:
            return pipeline("summarization", model=self.model_name)
        except Exception as e:
            logging.error(f"Erro ao carregar o modelo de sumarização: {e}")
            raise RuntimeError("Não foi possível inicializar o pipeline de sumarização.")

    def _get_token_limit(self) -> int:
        # Limite padrão para BART. Se mudar o modelo, ajuste aqui.
        model_token_limits = {
            "facebook/bart-large-cnn": 1024,
        }
        return model_token_limits.get(self.model_name, 900)

    def _split_into_sentences(self, text: str) -> List[str]:
        # Divide texto em sentenças, preservando pontuação.
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return [s.strip() for s in sentences if s.strip()]

    def _chunk_text(self, text: str) -> List[str]:
        # Cria chunks sem cortar palavras ou frases, até o limite de tokens.
        sentences = self._split_into_sentences(text)
        chunks = []
        current_chunk = []
        current_tokens = 0

        for sentence in sentences:
            sentence_tokens = len(sentence.split())
            if current_tokens + sentence_tokens > self.token_limit:
                # Fecha o chunk atual antes de passar do limite
                if current_chunk:
                    chunks.append(" ".join(current_chunk))
                current_chunk = [sentence]
                current_tokens = sentence_tokens
            else:
                current_chunk.append(sentence)
                current_tokens += sentence_tokens
        if current_chunk:
            chunks.append(" ".join(current_chunk))
        return chunks

    def _robust_summarize(self, text: str, max_length: Optional[int] = None, min_length: Optional[int] = None) -> str:
        max_length = max_length or 200
        min_length = min_length or 60
        try:
            result = self.summarizer(
                text,
                max_length=max_length,
                min_length=min_length,
                do_sample=False
            )
            return result[0]['summary_text']
        except Exception as e:
            logging.error(f"Erro na sumarização do chunk: {e}")
            # fallback: retorna parte do texto original
            return text[:max_length * 4]

    def summarize(self, transcript_path: str) -> Tuple[str, str]:
        if not os.path.exists(transcript_path):
            raise FileNotFoundError(f"Transcrição não encontrada: {transcript_path}")

        try:
            with open(transcript_path, encoding="utf-8") as f:
                text = f.read().strip()
        except Exception as e:
            logging.error(f"Erro ao ler a transcrição: {e}")
            raise RuntimeError("Não foi possível ler a transcrição.")

        if not text or len(text.split()) < 40:
            raise ValueError("Transcrição vazia ou muito curta.")

        chunks = self._chunk_text(text)
        chunk_count = len(chunks)

        if chunk_count == 1:
            max_len = min(400, max(100, len(text.split()) // 3))
            min_len = max(40, max_len // 3)
            summary = self._robust_summarize(text, max_length=max_len, min_length=min_len)
        else:
            chunk_summaries = []
            for chunk in chunks:
                chunk_len = len(chunk.split())
                max_len = min(200, max(80, chunk_len // 2))
                min_len = max(40, max_len // 2)
                summary = self._robust_summarize(chunk, max_length=max_len, min_length=min_len)
                chunk_summaries.append(summary)
            joined = " ".join(chunk_summaries)
            final_tokens = len(joined.split())
            max_len = min(450, max(120, final_tokens // 2))
            min_len = max(60, max_len // 2)
            summary = self._robust_summarize(joined, max_length=max_len, min_length=min_len)

        summary = re.sub(r'\s+', ' ', summary).strip()

        base_name = os.path.splitext(os.path.basename(transcript_path))[0]
        output_path = os.path.join(self.output_dir, f"{base_name}_summary.txt")
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(summary)
        except Exception as e:
            logging.error(f"Erro ao salvar o resumo: {e}")
            raise RuntimeError("Falha ao salvar o resumo.")

        return output_path, summary