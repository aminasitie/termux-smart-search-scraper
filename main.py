#!/usr/bin/env python3
"""
Termux Smart Search Scraper
Python Web Scraper yang dioptimalkan untuk Termux
Cari dan scrape data dari web dengan mudah
"""

import os
import sys
import csv
import time
import random
from datetime import datetime
from typing import List, Dict, Optional
import signal

# Handle keyboard interrupt gracefully
def signal_handler(sig, frame):
    print("\n\n⚠️  Proses dibatalkan oleh pengguna.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Try to import required libraries with error handling
try:
    from duckduckgo_search import DDGS
except ImportError:
    print("❌ Error: duckduckgo-search tidak terinstal.")
    print("   Jalankan: pip install duckduckgo-search")
    sys.exit(1)

try:
    import httpx
except ImportError:
    print("❌ Error: httpx tidak terinstal.")
    print("   Jalankan: pip install httpx")
    sys.exit(1)

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("❌ Error: beautifulsoup4 tidak terinstal.")
    print("   Jalankan: pip install beautifulsoup4")
    sys.exit(1)


class SmartSearchScraper:
    """
    Smart Search Scraper untuk Termux
    """
    
    def __init__(self):
        self.results = []
        self.user_agents = [
            'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 12; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36'
        ]
        
    def print_banner(self):
        """Display banner aplikasi"""
        banner = """
╔════════════════════════════════════════════════════════════╗
║           🔍 TERMUX SMART SEARCH SCRAPER 🔍               ║
║        Python Web Scraper untuk Termux Android            ║
╚════════════════════════════════════════════════════════════╝
        """
        print(banner)
        
    def get_user_input(self) -> Dict:
        """Mengambil input dari pengguna secara interaktif"""
        print("\n📝 INPUT PENCARIAN")
        print("=" * 50)
        
        # Kata kunci
        while True:
            keyword = input("\n🔎 Masukkan kata kunci pencarian: ").strip()
            if keyword:
                break
            print("⚠️  Kata kunci tidak boleh kosong!")
        
        # Jumlah hasil
        while True:
            try:
                num_results = input("📊 Jumlah hasil pencarian (default: 10): ").strip()
                num_results = int(num_results) if num_results else 10
                if 1 <= num_results <= 50:
                    break
                print("⚠️  Masukkan angka antara 1-50")
            except ValueError:
                print("⚠️  Masukkan angka yang valid!")
        
        # Format output
        print("\n📁 Format output:")
        print("   1. TXT (default)")
        print("   2. CSV")
        format_choice = input("Pilih format (1/2): ").strip()
        output_format = "csv" if format_choice == "2" else "txt"
        
        return {
            "keyword": keyword,
            "num_results": num_results,
            "format": output_format
        }
    
    def search_duckduckgo(self, keyword: str, num_results: int) -> List[Dict]:
        """Melakukan pencarian DuckDuckGo dan mengembalikan URL"""
        print(f"\n🔍 Mencari: '{keyword}'...")
        
        results = []
        try:
            with DDGS() as ddgs:
                search_results = list(ddgs.text(keyword, max_results=num_results))
                for i, result in enumerate(search_results):
                    results.append({
                        'url': result.get('href', ''),
                        'title': result.get('title', 'Tanpa Judul'),
                        'snippet': result.get('body', '')
                    })
                    print(f"   ✓ Ditemukan: {len(results)}/{num_results}")
        except Exception as e:
            print(f"\n⚠️  Warning: Pencarian terhenti setelah {len(results)} hasil")
            print(f"   Error: {str(e)[:100]}...")
        
        return results
    
    def extract_content(self, url: str, snippet: str = '') -> Dict:
        """Mengekstrak konten dari URL"""
        try:
            headers = {
                'User-Agent': random.choice(self.user_agents),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'Accept-Encoding': 'gzip, deflate, br',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            }
            
            with httpx.Client(timeout=15.0, follow_redirects=True) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, 'lxml')
                
                # Hapus elemen yang tidak diperlukan
                for element in soup(["script", "style", "nav", "footer", "header", "aside"]):
                    element.decompose()
                
                # Ekstrak judul
                title = ""
                if soup.title:
                    title = soup.title.string.strip() if soup.title.string else ""
                if not title:
                    h1 = soup.find('h1')
                    title = h1.get_text(strip=True) if h1 else "Tanpa Judul"
                
                # Ekstrak konten utama
                content = ""
                
                # Coba cari elemen konten utama
                main_content = soup.find(['main', 'article', 'div'], class_=lambda x: x and any(
                    word in str(x).lower() for word in ['content', 'article', 'post', 'entry']
                ))
                
                if main_content:
                    paragraphs = main_content.find_all('p')
                else:
                    paragraphs = soup.find_all('p')[:10]  # Ambil 10 paragraf pertama
                
                content = ' '.join([p.get_text(strip=True) for p in paragraphs if len(p.get_text(strip=True)) > 30])
                
                # Jika konten kosong, gunakan snippet dari search
                if not content and snippet:
                    content = snippet
                
                # Batasi panjang konten untuk menghemat RAM
                if len(content) > 500:
                    content = content[:500] + "..."
                
                return {
                    "url": url,
                    "title": title[:200],
                    "content": content,
                    "status": "success"
                }
        
        except httpx.TimeoutException:
            return {
                "url": url,
                "title": "Timeout",
                "content": snippet if snippet else "Website terlalu lama merespons (>15 detik)",
                "status": "timeout"
            }
        except httpx.HTTPStatusError as e:
            return {
                "url": url,
                "title": f"HTTP Error {e.response.status_code}",
                "content": snippet if snippet else f"Website memblokir akses atau tidak tersedia",
                "status": "http_error"
            }
        except Exception as e:
            return {
                "url": url,
                "title": "Error",
                "content": snippet if snippet else f"Gagal mengakses: {str(e)[:100]}",
                "status": "error"
            }
    
    def save_results_txt(self, keyword: str, results: List[Dict]) -> str:
        """Menyimpan hasil dalam format TXT"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"hasil_search/{keyword.replace(' ', '_')}_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Hasil Pencarian: {keyword}\n")
            f.write(f"Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Jumlah Hasil: {len(results)}\n")
            f.write("=" * 80 + "\n\n")
            
            for i, result in enumerate(results, 1):
                f.write(f"[{i}] {result['title']}\n")
                f.write(f"   Link: {result['url']}\n")
                f.write(f"   Status: {result['status']}\n")
                f.write(f"   Ringkasan: {result['content'][:300]}...\n")
                f.write("-" * 80 + "\n")
        
        return filename
    
    def save_results_csv(self, keyword: str, results: List[Dict]) -> str:
        """Menyimpan hasil dalam format CSV"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"hasil_search/{keyword.replace(' ', '_')}_{timestamp}.csv"
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["No", "Judul", "URL", "Status", "Ringkasan"])
            
            for i, result in enumerate(results, 1):
                writer.writerow([
                    i,
                    result['title'],
                    result['url'],
                    result['status'],
                    result['content'][:500]
                ])
        
        return filename
    
    def display_results(self, results: List[Dict]):
        """Menampilkan hasil di terminal"""
        print("\n" + "=" * 60)
        print("📊 HASIL PENCARIAN")
        print("=" * 60)
        
        successful = sum(1 for r in results if r['status'] == 'success')
        print(f"\n✅ Berhasil: {successful}/{len(results)}")
        
        for i, result in enumerate(results[:5], 1):
            print(f"\n[{i}] {result['title']}")
            print(f"    📍 {result['url'][:60]}...")
            if result['status'] == 'success':
                print(f"    📄 {result['content'][:100]}...")
            else:
                print(f"    ⚠️  {result['content'][:100]}")
        
        if len(results) > 5:
            print(f"\n    ... dan {len(results)-5} hasil lainnya")
    
    def run(self):
        """Menjalankan scraper utama"""
        self.print_banner()
        
        # Buat direktori hasil jika belum ada
        os.makedirs("hasil_search", exist_ok=True)
        
        # Ambil input pengguna
        config = self.get_user_input()
        
        print(f"\n🚀 Memulai scraping untuk: '{config['keyword']}'")
        print(f"   Jumlah target: {config['num_results']} hasil")
        print(f"   Format output: {config['format'].upper()}")
        
        # Lakukan pencarian
        search_results = self.search_duckduckgo(config['keyword'], config['num_results'])
        
        if not search_results:
            print("\n❌ Tidak ada hasil ditemukan. Coba kata kunci lain.")
            return
        
        print(f"\n📥 Mengambil konten dari {len(search_results)} URL...")
        
        # Scrape konten dari setiap URL
        results = []
        for i, search_result in enumerate(search_results, 1):
            print(f"\n   [{i}/{len(search_results)}] Memproses: {search_result['url'][:50]}...")
            
            result = self.extract_content(search_result['url'], search_result.get('snippet', ''))
            results.append(result)
            
            # Tampilkan status
            if result['status'] == 'success':
                print(f"      ✓ Berhasil: {result['title'][:40]}...")
            else:
                print(f"      ⚠️  Gagal: {result['content'][:40]}...")
            
            # Delay acak untuk menghindari blocking
            time.sleep(random.uniform(0.5, 1.5))
        
        # Tampilkan hasil
        self.display_results(results)
        
        # Simpan hasil
        print(f"\n💾 Menyimpan hasil...")
        
        if config['format'] == 'csv':
            filename = self.save_results_csv(config['keyword'], results)
        else:
            filename = self.save_results_txt(config['keyword'], results)
        
        print(f"\n✅ Hasil disimpan ke: {filename}")
        
        # Tampilkan ringkasan
        print("\n" + "=" * 60)
        print("📈 RINGKASAN")
        print("=" * 60)
        print(f"🔍 Kata Kunci: {config['keyword']}")
        print(f"📊 Total URL: {len(search_results)}")
        print(f"✅ Berhasil scrape: {sum(1 for r in results if r['status'] == 'success')}")
        print(f"⚠️  Gagal scrape: {sum(1 for r in results if r['status'] != 'success')}")
        print(f"📁 File output: {filename}")
        print(f"💾 Lokasi: {os.path.abspath(filename)}")
        
        print("\n🎉 Scraping selesai!")


def main():
    """Fungsi utama"""
    try:
        scraper = SmartSearchScraper()
        scraper.run()
    except KeyboardInterrupt:
        print("\n\n⚠️  Program dihentikan oleh pengguna.")
    except Exception as e:
        print(f"\n❌ Error tidak terduga: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
