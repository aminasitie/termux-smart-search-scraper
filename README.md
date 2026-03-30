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

- Android dengan Termux terinstal (download dari [F-Droid](https://f-droid.org/packages/com.termux/) atau Play Store)
- Koneksi internet
- Minimal 100MB ruang penyimpanan bebas

## 🚀 Instalasi Cepat (5 Langkah)

Ikuti langkah-langkah berikut **secara berurutan**:

```bash
# Langkah 1: Instal Git
pkg install git -y

# Langkah 2: Clone Repositori
git clone https://github.com/aminasitie/termux-smart-search-scraper.git

# Langkah 3: Masuk ke Direktori
cd termux-smart-search-scraper

# Langkah 4: Jalankan Instalasi Otomatis
bash install.sh

# Langkah 5: Jalankan Scraper
python main.py
```

## 📖 Cara Penggunaan

### Menjalankan Program
```bash
python main.py
```

### Input yang Diperlukan
1. **Kata kunci pencarian**: Contoh: "harga laptop bekas"
2. **Jumlah hasil**: Berapa banyak hasil yang ingin di-scrape (1-50)
3. **Format output**: Pilih TXT atau CSV

### Lokasi Hasil
Hasil disimpan di folder `hasil_search/` dengan format:
- TXT: `hasil_search/kata_kunci_tanggal.txt`
- CSV: `hasil_search/kata_kunci_tanggal.csv`

## 🔧 Troubleshooting

### Jika `install.sh` Gagal

Jika instalasi otomatis gagal, instal manual:

```bash
# Instal dependensi sistem
pkg install python python-pip git libxml2 libxslt -y

# Setup storage (opsional)
termux-setup-storage

# Instal paket Python
pip install googlesearch-python httpx beautifulsoup4 lxml

# Atau gunakan flag ini jika error PEP 668
pip install --break-system-packages googlesearch-python httpx beautifulsoup4 lxml
```

### Masalah Umum

1. **"externally-managed-environment"**
   ```bash
   pip install --break-system-packages -r requirements.txt
   ```

2. **"command not found: pkg"**
   - Pastikan menggunakan Termux dari F-Droid atau Play Store

3. **"pip not found"**
   ```bash
   pkg install python-pip -y
   ```

4. **"Permission denied"**
   ```bash
   chmod +x install.sh
   bash install.sh
   ```

5. **Module not found error**
   ```bash
   pip install --break-system-packages googlesearch-python httpx beautifulsoup4 lxml
   ```

## 📊 Contoh Output

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

## 📁 Struktur Direktori

```
termux-smart-search-scraper/
├── install.sh          # Skrip instalasi otomatis
├── requirements.txt    # Daftar library Python
├── main.py             # Skrip utama scraper
├── README.md           # Dokumentasi ini
└── hasil_search/       # Folder hasil (otomatis dibuat)
```

## ⚡ Tips Optimasi Termux

1. **Hemat RAM**: Maksimal 50 hasil untuk menghindari memory overflow
2. **Hemat Storage**: Konten dibatasi 500 karakter per hasil
3. **Hemat Baterai**: Delay antar request mencegah CPU spike
4. **Storage Android**: Hasil di internal storage via termux-setup-storage

## 📚 Library yang Digunakan

| Library | Versi | Fungsi |
|---------|-------|--------|
| googlesearch-python | 1.2.1 | Pencarian Google |
| httpx | 0.27.0 | HTTP client |
| beautifulsoup4 | 4.12.3 | Parsing HTML |
| lxml | 5.1.0 | Parser HTML cepat |

## ⚠️ Disclaimer

- Gunakan dengan bijak dan bertanggung jawab
- Hormati robots.txt dan ToS setiap website
- Jangan untuk scraping massal yang membebani server
- Hanya untuk penggunaan pribadi

## 📞 Kontak

- **GitHub Issues**: https://github.com/aminasitie/termux-smart-search-scraper/issues
- **Email**: aminasitie@gmail.com

## 📄 Lisensi

MIT License

---

**Dibuat dengan ❤️ untuk komunitas Termux Indonesia**
