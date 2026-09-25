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

# ==================== MENCARI DATA BERDASARKAN SLUG (UNIT 5.3) ====================

@app.get("/blog/{slug}")
def baca_detail_artikel(
    request: Request, 
    slug: str = Path(..., min_length=3, max_length=50, pattern="^[a-z0-9-]+$")
):
    # 1. Ambil seluruh daftar artikel asli dari file posts.json
    semua_artikel = ambil_semua_artikel()

    # 2. Lakukan pencarian satu per satu di dalam daftar menggunakan looping for
    artikel_ditemukan = None
    for artikel in semua_artikel:
        if artikel["slug"] == slug:
            artikel_ditemukan = artikel
            break # Jika sudah cocok dan ketemu, langsung hentikan perulangan pencarian

    # 3. Antisipasi jika slug-nya legal (lolos REGEX) tetapi artikelnya tidak ada di posts.json
    if artikel_ditemukan is None:
        # Lempar pesan eror status 404 (Halaman Tidak Ditemukan) secara resmi
        raise HTTPException(status_code=404, detail="Maaf, tulisan blog tidak ditemukan")

    # 4. Jika ketemu, kirimkan data artikel utuh tersebut (sementara berbentuk data JSON dulu)
    return artikel_ditemukan
