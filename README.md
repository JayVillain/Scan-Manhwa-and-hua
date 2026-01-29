## 🚀 Cara Penggunaan

Bagian ini menjelaskan cara menjalankan script secara manual untuk mengambil daftar URL chapter.

### 1. Instalasi Dependency
Jalankan perintah ini satu kali untuk menginstal pustaka yang dibutuhkan:
```bash
pip install requests beautifulsoup4
```
### 2. Menjalankan Scanner

 Scan semua chapter
```bash
python scan_series.py https://example.com/manga/solo-leveling
```
Scan range chapter
```bash
python scan_series.py https://example.com/manga/solo-leveling --from 10 --to 30
```

Scan dari chapter tertentu sampai terakhir
```bash
python scan_series.py https://example.com/manga/solo-leveling --from 50
```

Scan satu chapter saja
```bash
python scan_series.py https://example.com/manga/solo-leveling --only 73
```

Scan chapter terbaru
```bash
python scan_series.py https://example.com/manga/solo-leveling --latest 5
```

### Output

File chapters.txt akan dibuat

Isinya hanya URL chapter

Siap dipakai oleh downloader image

### Note

Script ini tidak menjalankan JavaScript

Tidak cocok untuk infinite scroll JS

Cocok untuk mayoritas situs manga/manhwa statis
