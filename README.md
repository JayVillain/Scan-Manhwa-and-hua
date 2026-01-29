# 📚 Universal Manhwa Series Scanner

Tool Python untuk **scan daftar chapter manhwa/manga** dari halaman **series** secara otomatis.

Tool ini hanya bertugas **mengambil URL chapter**, bukan mendownload gambar.  
Hasil scan disimpan ke file `chapters.txt` dan **siap digunakan oleh tool downloader lain**.

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

## 🧰 Requirement

- Python **3.8+**

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

2️⃣ Scan RANGE chapter
python scan_series.py <URL_SERIES> --from 10 --to 30
Contoh:

python scan_series.py https://manhwaboysz.com/manga/solo-leveling --from 10 --to 30
Artinya:
Hanya Chapter 10 sampai Chapter 30 yang disimpan ke chapters.txt.

3️⃣ Scan dari chapter tertentu sampai terakhir
python scan_series.py <URL_SERIES> --from 50
Artinya:
Chapter 50 sampai chapter terakhir.

4️⃣ Scan SATU chapter saja
python scan_series.py <URL_SERIES> --only 73
Artinya:
Hanya Chapter 73.

5️⃣ Scan N chapter TERBARU
python scan_series.py <URL_SERIES> --latest 5
Artinya:
Ambil 5 chapter terbaru saja.

📄 Output
Tool ini akan menghasilkan file:

chapters.txt
Contoh isi file (dummy):

https://manhwaboysz.com/solo-leveling/chapter-1
https://manhwaboysz.com/solo-leveling/chapter-2
https://manhwaboysz.com/solo-leveling/chapter-3
File ini siap langsung digunakan oleh downloader image/manhwa.

🔄 Contoh Workflow Lengkap
1. Scan series
   python scan_series.py https://manhwaboysz.com/manga/solo-leveling --from 1 --to 20

2. Download chapter (menggunakan tool downloader terpisah)
   python manhwa_downloader.py chapters.txt
🌐 Website yang Umumnya Didukung
Tool ini bekerja pada website manga/manhwa yang:

Memiliki halaman series

Menyediakan daftar chapter

Menggunakan kata "chapter" pada URL atau teks

Contoh struktur URL (dummy):

/solo-leveling/chapter-1
/solo-leveling/chapter-176.5
⚠️ Batasan
Tool ini tidak mendukung:

❌ Infinite scroll berbasis JavaScript

❌ Chapter list yang dimuat via API JavaScript

❌ Website tanpa indikator kata "chapter"

Untuk kasus tersebut, diperlukan browser automation seperti Playwright atau Selenium.

🧠 Catatan Teknis
Scan dilakukan sepenuhnya terlebih dahulu

Filter diterapkan setelah semua chapter terkumpul

Urutan chapter selalu akurat

Mendukung nomor chapter desimal (contoh: 176.5)

📌 Etika Penggunaan
Gunakan tool ini dengan bijak:

Jangan melakukan flood request

Hormati server target

Pastikan penggunaan sesuai izin & hukum yang berlaku

