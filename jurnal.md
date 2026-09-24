# fastapi-beginner-blog
Learning framework FastAPI by building a fully static blog

#### Initial commit: modified project basic files and push it to github

        modified:   .gitignore
        new file:   jurnal.md


## BAB 1: Fondasi & Instalasi Lingkungan Kerja

#### Unit 1.1: Pengenalan Arsitektur FastAPI & Mengapa Cocok untuk Static Blog
        Pass

#### Unit 1.2: Spesifikasi OS (Windows 10) & Standarisasi Workspace di `D:\devspace\--fastapi--`
        Pass

#### Unit 1.3: Setup Environment di Windows (Instalasi Python & Konfigurasi Virtual Environment)

        fastapi-beginner-blog
        |-- LICENSE
        |-- README.md
        |-- jurnal.md
        `-- venv313014
            |-- Include
            |-- Lib
            |-- Scripts
            `-- pyvenv.cfg

#### Unit 1.4: Instalasi FastAPI, Uvicorn, dan Dependensi Awal via Terminal Windows

        $ pip install fastapi uvicorn jinja2
        ...
        Installing collected packages: typing-extensions, MarkupSafe, idna, h11, click, annotated-types, ann
        otated-doc, uvicorn, typing-inspection, pydantic-core, jinja2, anyio, starlette, pydantic, fastapi
        Successfully installed MarkupSafe-3.0.3 annotated-doc-0.0.5 annotated-types-0.8.0 anyio-4.15.1 click
        -8.5.0 fastapi-0.141.1 h11-0.16.0 idna-3.20 jinja2-3.1.6 pydantic-2.13.5 pydantic-core-2.46.5 starle
        tte-1.7.0 typing-extensions-4.16.0 typing-inspection-0.4.4 uvicorn-0.53.0

        [notice] A new release of pip is available: 24.2 -> 26.2.1
        [notice] To update, run: python.exe -m pip install --upgrade pip
        (venv313014)
        Asus@DESKTOP-IC0RV3J MINGW64 /d/devspace/--FastAPI--/fastapi-beginner/project/fastapi-beginner-blog (main)
        $ pip list
        Package           Version
        ----------------- -------
        annotated-doc     0.0.5
        annotated-types   0.8.0
        anyio             4.15.1
        click             8.5.0
        fastapi           0.141.1
        h11               0.16.0
        idna              3.20
        Jinja2            3.1.6
        MarkupSafe        3.0.3
        pip               24.2
        pydantic          2.13.5
        pydantic_core     2.46.5
        starlette         1.7.0
        typing_extensions 4.16.0
        typing-inspection 0.4.4
        uvicorn           0.53.0

        $ python.exe -m pip install --upgrade pip
        ...
              Successfully uninstalled pip-24.2
        Successfully installed pip-26.2.1

#### Unit 1.5: Hello World Pertama & Memahami Lifecycle Uvicorn Server

        modified:   jurnal.md
        new file:   main.py


## BAB 2: Struktur Folder & Manajemen File Statis

#### Unit 2.1: Merancang Arsitektur Folder Standar Industri (`src/`, `static/`, `templates/`)

        modified:   jurnal.md
        renamed:    main.py -> src/main.py
        new file:   static/css/style.css
        new file:   static/js/script.js
        new file:   templates/index.html

        .
        |-- LICENSE
        |-- README.md
        |-- jurnal.md
        |-- src
        |   `-- main.py
        |-- static
        |   |-- css
        |   |   `-- style.css
        |   |-- img
        |   `-- js
        |       `-- script.js
        `-- templates
            `-- index.html


#### Unit 2.2: Konfigurasi `StaticFiles` di FastAPI (Menghubungkan CSS, JS, dan Gambar)

        modified:   src/main.py
        modified:   static/css/style.css

#### Unit 2.3: Membuat Halaman HTML Mentah Pertama Tanpa Templating

        modified:   jurnal.md
        modified:   src/main.py
        modified:   templates/index.html


## BAB 3: Menguasai Templating Engine (Jinja2)

#### Unit 3.1: Integrasi `Jinja2Templates` ke dalam FastAPI

        modified:   jurnal.md
        modified:   src/main.py

#### Unit 3.2: Teknik *Template Inheritance* (Membuat `base.html` agar kode tidak duplikat)

        modified:   jurnal.md
        new file:   templates/base.html
        modified:   templates/index.html

#### Unit 3.3: Mengirim Data dari Backend Python ke Halaman HTML (*Context Passing*)

        modified:   jurnal.md
        modified:   src/main.py
        modified:   templates/index.html

#### Unit 3.4: Logika Jinja2 di HTML (Looping daftar artikel dan Kondisional IF)

        modified:   jurnal.md
        modified:   src/main.py
        modified:   templates/index.html

## BAB 4: Manajemen Konten Blog Statis (Database File)

#### Unit 4.1: Memilih Format Data Statis (Mengapa JSON/Markdown cocok untuk blog statis)
        Pass

#### Unit 4.2: Membuat 'Mock Database' Menggunakan File JSON

        modified:   jurnal.md
        new file:   src/posts.json

#### Unit 4.3: Membuat Fungsi Python untuk Membaca File Data Artikel

        modified:   jurnal.md
        modified:   src/main.py