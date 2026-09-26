import json
# Tambahkan alat bernama HTTPException dari modul fastapi untuk menangani eror 404
from fastapi import FastAPI, Request, Path, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

def ambil_semua_artikel():
    with open("src/posts.json", "r", encoding="utf-8") as file:
        data_artikel = json.load(file)
    return data_artikel

@app.get("/")
def baca_utama(request: Request):
    artikel_dari_json = ambil_semua_artikel()
    data_kiriman = {
        "nama_pemilik": "Transformasi Anak Bangsa",
        "slogan": "Berbagai ilmu, pengetahuan, dan keterampilan tinggi bagi Genius Bangsa yang ingin bertumbuh.",
        "daftar_artikel": artikel_dari_json
    }
    return templates.TemplateResponse(request=request, name="index.html", context={"data": data_kiriman})


# ==================== KODE RAMPING & BERSIH (UNIT 5.11) ====================

@app.get("/")
def baca_utama(request: Request):
    artikel_dari_json = ambil_semua_artikel()
    data_kiriman = {
        "nama_pemilik": "Transformasi Anak Bangsa",
        "slogan": "Berbagai ilmu, pengetahuan, dan keterampilan tinggi bagi Genius Bangsa yang ingin bertumbuh.",
        "daftar_artikel": artikel_dari_json
    }
    # Teks nama_blog yang berulang sudah dihapus dari context
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"data": data_kiriman}
    )

@app.get("/about")
def baca_tentang(request: Request):
    # Context kembali kosong dan bersih
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={}
    )

@app.get("/blog/{slug}")
def baca_detail_artikel(
    request: Request, 
    slug: str = Path(..., min_length=3, max_length=50, pattern="^[a-z0-9-]+$")
):
    semua_artikel = ambil_semua_artikel()
    artikel_ditemukan = None
    for artikel in semua_artikel:
        if artikel["slug"] == slug:
            artikel_ditemukan = artikel
            break
            
    if artikel_ditemukan is None:
        raise HTTPException(status_code=404, detail="Maaf, tulisan blog tidak ditemukan")
        
    # Teks nama_blog yang berulang sudah dihapus dari context
    return templates.TemplateResponse(
        request=request,
        name="detail.html",
        context={"artikel": artikel_ditemukan}
    )
