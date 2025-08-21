import os
import subprocess
import json

class YouTubeDownloader:
    def __init__(self, output_dir="data/downloads"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def download_audio(self, url: str) -> str:
        """Baixa o áudio do vídeo do YouTube como mp3."""
        # Obtém informações do vídeo
        info_cmd = [
            'yt-dlp', '--dump-json', '--no-playlist', url
        ]
        result = subprocess.run(info_cmd, capture_output=True, text=True, check=True)
        video_info = json.loads(result.stdout)
        title = video_info.get('title', 'video')
        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
        output_filename = f"{safe_title}.mp3"
        output_path = os.path.join(self.output_dir, output_filename)

        # Baixa o áudio
        download_cmd = [
            'yt-dlp', '-f', 'bestaudio/best',
            '--extract-audio', '--audio-format', 'mp3', '--audio-quality', '192k',
            '-o', output_path, '--no-playlist', url
        ]
        subprocess.run(download_cmd, check=True)
        if os.path.exists(output_path):
            return output_path
        # Procura por qualquer mp3 se não achou pelo nome
        for file in os.listdir(self.output_dir):
            if file.endswith('.mp3'):
                return os.path.join(self.output_dir, file)
        return None