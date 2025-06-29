import os
import subprocess
import json

def download_audio(url: str, output_dir: str = None) -> str:
    # Define o diretório downloads dentro de src
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(__file__), 'downloads')
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # Primeiro, obtém informações do vídeo
        info_cmd = [
            'yt-dlp',
            '--dump-json',
            '--no-playlist',
            url
        ]
        
        result = subprocess.run(info_cmd, capture_output=True, text=True, check=True)
        video_info = json.loads(result.stdout)
        
        # Extrai o título para usar como nome do arquivo
        title = video_info.get('title', 'video')
        # Remove caracteres inválidos do nome do arquivo
        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
        output_filename = f"{safe_title}.mp3"
        output_path = os.path.join(output_dir, output_filename)
        
        # Comando para baixar o áudio
        download_cmd = [
            'yt-dlp',
            '-f', 'bestaudio/best',
            '--extract-audio',
            '--audio-format', 'mp3',
            '--audio-quality', '192k',
            '-o', output_path,
            '--no-playlist',
            url
        ]
        
        print("Executando download...")
        subprocess.run(download_cmd, check=True)
        
        # Verifica se o arquivo foi criado
        if os.path.exists(output_path):
            return output_path
        else:
            # Se não encontrou com o nome exato, procura por arquivos .mp3 na pasta
            for file in os.listdir(output_dir):
                if file.endswith('.mp3'):
                    return os.path.join(output_dir, file)
            
            return None
            
    except subprocess.CalledProcessError as e:
        print(f"Erro no download: {e}")
        if e.stderr:
            print(f"Detalhes: {e.stderr}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None