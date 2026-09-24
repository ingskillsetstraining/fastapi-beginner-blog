# main.py

# 1. Ambil kelas FastAPI dari dalam modul fastapi yang sudah kita instal di dalam venv313014
from fastapi import FastAPI

# 2. Instansiasi klas FastAPI: membuat wujud nyata dari kelas FastAPI 
# sebagai sebuah object aplikasi web utama. Object tersebut kita namai 'app'
app = FastAPI()

# 3. Buat aturan jalan: jika ada pengunjung membuka halaman 
# utama, misal ("http://127.0.0.1:8000/") dengan metode GET...
@app.get("/")
# 4. ...maka jalankan fungsi bernama 'baca_halo' di bawah ini
def baca_halo():
    # 5. Kirimkan balasan berupa data teks terstruktur (JSON) ke layar browser mereka
    return {"pesan": "Halo Dunia dari FastAPI"}

