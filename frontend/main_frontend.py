from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Simulação (você vai trocar pela lógica real da API de resumo)
from app.summarizer import gerar_resumo

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def form_post(request: Request, youtube_url: str = Form(...)):
    resumo = gerar_resumo(youtube_url)  # Chame sua função real aqui
    return templates.TemplateResponse("index.html", {"request": request, "summary": resumo})
