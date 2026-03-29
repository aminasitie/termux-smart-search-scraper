# 🔍 Termux Smart Search Scraper

Python Web Scraper yang dioptimalkan untuk Termux Android. Mencari informasi berdasarkan kata kunci menggunakan Google Search dan mengekstrak data dari hasil pencarian.

## ✨ Fitur

- **Pencarian Berbasis Kata Kunci**: Cari informasi dengan kata kunci apapun
- **Ekstraksi Konten Otomatis**: Mengambil judul, link, dan ringkasan konten
- **Output Bersih**: Simpan hasil dalam format TXT atau CSV
- **Optimasi Termux**: Efisien dalam penggunaan RAM dan storage
- **Error Handling Cerdas**: Tidak berhenti meskipun beberapa website memblokir akses
- **Auto-Installation**: Setup lengkap dalam satu perintah

## 📋 Prasyarat

- Android dengan Termux terinstal
- Koneksi internet
- Minimal 100MB ruang penyimpanan bebas

## 🚀 Instalasi Cepat

Ikuti langkah-langkah berikut **secara berurutan**:

### Langkah 1: Instal Git
```bash
pkg install git -y
```

### Langkah 2: Clone Repositori
```bash
git clone https://github.com/aminasitie/termux-smart-search-scraper.git
```

### Langkah 3: Masuk ke Direktori
```bash
cd termux-smart-search-scraper
```

### Langkah 4: Jalankan Instalasi Otomatis
```bash
bash install.sh
```

### Langkah 5: Jalankan Scraper
```bash
python main.py
```

## 📖 Panduan Penggunaan

### 1. Menjalankan Program
Setelah instalasi, jalankan dengan:
```bash
python main.py
```

### 2. Memasukkan Kata Kunci
Program akan meminta input:
- **Kata kunci pencarian**: Contoh: "harga laptop bekas"
- **Jumlah hasil**: Berapa banyak hasil yang ingin di-scrape (1-50)
- **Format output**: Pilih TXT atau CSV

### 3. Melihat Hasil
Hasil akan disimpan di folder `hasil_search/` dengan format:
- TXT: `hasil_search/kata_kunci_tanggal.txt`
- CSV: `hasil_search/kata_kunci_tanggal.csv`

### 4. Contoh Output
**Format TXT:**
```
Hasil Pencarian: harga laptop bekas
Tanggal: 2026-03-30 12:00:00
Jumlah Hasil: 10
================================================================================

[1] Laptop Bekas Murah - Toko Online
   Link: https://contoh.com/laptop-bekas
   Status: success
   Ringkasan: Jual laptop bekas dengan harga terjangkau...
--------------------------------------------------------------------------------
```

**Format CSV:**
```csv
No,Judul,URL,Status,Ringkasan
1,Laptop Bekas Murah,https://contoh.com/laptop-bekas,success,Jual laptop bekas...
```

## 🔧 Struktur Direktori

```
termux-smart-search-scraper/
├── install.sh          # Skrip instalasi otomatis
├── requirements.txt    # Daftar library Python
├── main.py            # Skrip utama scraper
├── README.md          # Dokumentasi ini
└── hasil_search/      # Folder hasil (otomatis dibuat)
```

## 🐛 Troubleshooting

### Masalah Umum:

1. **"command not found: pkg"**
   - Pastikan Anda menggunakan Termux dari F-Droid atau Play Store
   - Bukan Termux dari Google Play (sudah tidak diupdate)

2. **"pip not found"**
   ```bash
   pkg install python-pip -y
   ```

3. **"Permission denied" saat menjalankan install.sh**
   ```bash
   chmod +x install.sh
   bash install.sh
   ```

4. **Program berhenti di tengah jalan**
   - Beberapa website mungkin memblokir akses
   - Program akan melanjutkan ke URL berikutnya
   - Cek file hasil untuk melihat URL yang berhasil

5. **Tidak ada hasil yang ditemukan**
   - Coba kata kunci yang lebih spesifik
   - Periksa koneksi internet
   - Coba kurangi jumlah hasil

## 📊 Contoh Penggunaan

```bash
# Contoh 1: Cari harga laptop
python main.py
# Input: "harga laptop bekas", 10, TXT

# Contoh 2: Cari resep masakan
python main.py  
# Input: "resep nasi goreng", 5, CSV

# Contoh 3: Cari berita terkini
python main.py
# Input: "berita teknologi terbaru", 15, TXT
```

## ⚡ Tips Optimasi untuk Termux

1. **Hemat RAM**: Program dibatasi maksimal 50 hasil untuk menghindari memory overflow
2. **Hemat Storage**: Output dibatasi panjang konten untuk menghemat ruang
3. **Hemat Baterai**: Delay antar request mencegah CPU spike
4. **Storage Android**: Hasil disimpan di internal storage melalui termux-setup-storage

## 🛡️ Legal Disclaimer

- Gunakan scraper ini dengan bijak dan bertanggung jawab
- Hormati robots.txt dan terms of service setiap website
- Jangan gunakan untuk scraping massal yang dapat membebani server
- Hasil scraping hanya untuk penggunaan pribadi

## 📝 Library yang Digunakan

- **googlesearch-python**: Untuk pencarian Google
- **httpx**: HTTP client modern (async-ready)
- **beautifulsoup4**: Parsing HTML
- **lxml**: Parser HTML cepat

## 📞 Kontak & Dukungan

- **GitHub Issues**: https://github.com/aminasitie/termux-smart-search-scraper/issues
- **Email**: aminasitie@gmail.com

## 📄 Lisensi

MIT License - Bebas digunakan dan dimodifikasi.

---

**Dibuat dengan ❤️ untuk komunitas Termux Indonesia**
