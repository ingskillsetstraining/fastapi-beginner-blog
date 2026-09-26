# src/blog.py

import json
# 1. Impor APIRouter, Path, dan HTTPException dari modul fastapi
from fastapi import APIRouter, Request, Path, HTTPException
from fastapi.templating import Jinja2Templates

# 2. Inisialisasi objek APIRouter khusus untuk mengurus rute blog
router = APIRouter()

# 3. Hubungkan ke mesin templating Jinja2 (naik satu folder ke templates/)
templates = Jinja2Templates(directory="templates")

def ambil_semua_artikel():
    with open("src/posts.json", "r", encoding="utf-8") as file:
        data_artikel = json.load(file)
    return data_artikel

# ==================== RUTE YANG DIPINDAHKAN KEMARI ====================

# 4. Ganti dekorator @app.get menjadi @router.get
@router.get("/blog/{slug}")
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
        
    return templates.TemplateResponse(
        request=request,
        name="detail.html",
        context={"artikel": artikel_ditemukan}
    )
