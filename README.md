## 🚀 Cara Penggunaan

Bagian ini menjelaskan cara menjalankan script secara manual untuk mengambil daftar URL chapter.

### 1. Instalasi Dependency
Jalankan perintah ini satu kali untuk menginstal pustaka yang dibutuhkan:
```bash
pip install requests beautifulsoup4
2. Menjalankan ScannerGunakan file scan_series.py diikuti dengan URL target dan parameter yang diinginkan:SkenarioPerintahScan Semua Chapterpython scan_series.py https://example.com/manga/solo-levelingRentang Chapter (Range)python scan_series.py https://example.com/manga/solo-leveling --from 10 --to 30Dari Chapter N ke Ataspython scan_series.py https://example.com/manga/solo-leveling --from 50Satu Chapter Spesifikpython scan_series.py https://example.com/manga/solo-leveling --only 73N Chapter Terbarupython scan_series.py https://example.com/manga/solo-leveling --latest 5📂 OutputSetelah proses scan selesai, script akan menghasilkan file chapters.txt yang berisi daftar URL chapter. File ini dirancang agar siap digunakan langsung oleh program image downloader.🛠️ Catatan TeknisStatic Content Only: Script bekerja dengan membedah HTML statis.No JS Engine: Tidak mendukung situs yang memerlukan eksekusi JavaScript (seperti infinite scroll berat).Compatibility: Optimal untuk mayoritas situs manga/manhwa dengan struktur HTML statis.
