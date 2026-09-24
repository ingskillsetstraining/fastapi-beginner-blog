# main.py

# 1. Ambil kelas FastAPI dan alat StaticFiles dari modul fastapi
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# 2. Buat objek aplikasi web utama
app = FastAPI()

# 3. Beri tahu FastAPI lokasi folder statis kita
app.mount("/static", StaticFiles(directory="static"), name="static")

# 4. Aturan rute halaman utama yang sudah kita buat sebelumnya
@app.get("/")
def baca_halo():
    return {"pesan": "Halo Dunia dari FastAPI di dalam folder src"}
