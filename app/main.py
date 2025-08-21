from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.services.downloader import YouTubeDownloader
from app.services.transcriber import AudioTranscriber
from app.services.summarizer import TextSummarizer
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")

downloader = YouTubeDownloader()
transcriber = AudioTranscriber()
summarizer = TextSummarizer()

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "summary": None, "error": None})

@app.post("/", response_class=HTMLResponse)
async def summarize_youtube(request: Request, youtube_url: str = Form(...)):
    summary = None
    error = None
    try:
        # 1. Baixar
        audio_path = downloader.download_audio(youtube_url)
        # 2. Transcrever
        transcript_path = transcriber.transcribe_audio(audio_path)
        # 3. Resumir
        summary_path, summary = summarizer.summarize(transcript_path)
    except Exception as e:
        error = str(e)
    return templates.TemplateResponse("index.html", {"request": request, "summary": summary, "error": error})