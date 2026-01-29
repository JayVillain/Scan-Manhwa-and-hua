# Scan-Manhwa-and-hua
# 📚 Universal Manhwa Series Scanner

Tool Python sederhana untuk **scan daftar chapter manhwa/manga** dari halaman **series** di berbagai website (Shinigami, Manhwalist, Komikcast, Sektekomik, dll).

Tool ini akan:
- Mengambil **semua URL chapter**
- Mendukung **pagination otomatis**
- Menyediakan **filter range chapter**
- Menyimpan hasil ke file `chapters.txt`
- Siap dipakai oleh downloader image

---

## ✨ Fitur

- ✅ Scan series dari **1 URL**
- ✅ Pagination otomatis (`?page=2`, `?page=3`, dst)
- ✅ Deteksi chapter secara universal (tanpa hardcode website)
- ✅ Filter chapter saat scan:
  - Range (`--from`, `--to`)
  - Satu chapter (`--only`)
  - Chapter terbaru (`--latest`)
- ✅ Output rapi & terurut
- ✅ Cocok untuk workflow downloader manga/manhwa

---

## 🧰 Dependency

Python 3.8+ direkomendasikan.

Install dependency (1x saja):

```bash
pip install requests beautifulsoup4

🚀 Cara Penggunaan
1️⃣ Scan SEMUA chapter (default)
python scan_series.py <URL_SERIES>


Contoh (URL dummy):

python scan_series.py https://manhwaboysz.com/manga/solo-leveling


Hasil:

Semua chapter discan

Pagination otomatis

File chapters.txt dibuat
