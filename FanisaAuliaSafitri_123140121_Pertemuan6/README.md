# Aplikasi Manajemen Matakuliah - Pyramid API

### 1. Deskripsi Proyek
Aplikasi ini adalah API sederhana untuk manajemen data matakuliah yang dibangun menggunakan framework **Pyramid**, **SQLAlchemy** sebagai ORM, dan **Alembic** untuk migrasi database. Aplikasi ini mendukung operasi CRUD (Create, Read, Update, Delete) untuk data matakuliah.

### 2. Cara Instalasi
Langkah-langkah untuk menyiapkan lingkungan pengembangan:

* **Membuat Virtual Environment:**
    ```bash
    python -m venv env
    ```
* **Aktivasi Virtual Environment:**
    * Windows: `.\env\Scripts\activate`
    * Linux/Mac: `source env/bin/activate`
* **Instalasi Dependensi:**
    ```bash
    pip install -e .
    pip install pyramid_tm zope.sqlalchemy alembic
    ```
* **Konfigurasi Database:**
    Pastikan file `development.ini` dan `alembic.ini` sudah dikonfigurasi menggunakan SQLite:
    `sqlalchemy.url = sqlite:///%(here)s/matakuliah.sqlite`.

### 3. Cara Menjalankan
* **Menjalankan Migrasi:**
    ```bash
    alembic upgrade head
    ```
* **Menjalankan Server:**
    ```bash
    pserve development.ini --reload
    ```

### 4. API Endpoints
Berikut adalah dokumentasi endpoint yang tersedia:
<img width="1893" height="117" alt="image" src="https://github.com/user-attachments/assets/bc56e308-4f91-4731-8630-ec56939cfcaf" />

#### A. Mendapatkan Semua Matakuliah
**Request:**
`GET http://localhost:6543/api/matakuliah`
