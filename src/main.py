# main.py

# 1. Ambil kelas utama, alat file statis, dan alat pengirim file HTML
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# 2. Buat objek aplikasi web utama
app = FastAPI()

# 3. Hubungkan folder aset statis (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 4. Aturan rute halaman utama
@app.get("/")
def baca_utama():
    # 5. Kirim file fisik index.html yang ada di folder templates ke browser
    return FileResponse("templates/index.html")

