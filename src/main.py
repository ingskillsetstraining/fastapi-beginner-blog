# main.py

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def baca_utama(request: Request):
    # 1. Buat data kiriman di dalam kamus Python (Dictionary)
    data_kiriman = {
        "nama_pemilik": "Transformasi Anak Bangsa",
        "slogan": "Berbagai ilmu, pengetahuan, dan keterampilan tinggi bagi Genius Bangsa yang ingin bertumbuh."
    }

    # 2. Masukkan kamus data tersebut ke dalam parameter 'context'
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"data": data_kiriman} # <-- Kita bungkus dengan kata kunci 'data'
    )
