from downloader import download_audio
from transcriber import transcribe_audio

def main():
    url = input("Cole a URL do YouTube: ").strip()
    
    # 1. Download
    print("Baixando áudio...")
    audio_path = download_audio(url)
    
    if not audio_path:
        print("Falha no download")
        return
    
    # 2. Transcrição
    print("Transcrevendo áudio...")
    try:
        transcript_path = transcribe_audio(audio_path)
        print(f"Transcrição salva em: {transcript_path}")
    except Exception as e:
        print(f"Erro na transcrição: {e}")

if __name__ == "__main__":
    main()