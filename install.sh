#!/bin/bash
# Termux Smart Search Scraper - Installation Script
# Optimized for Termux and Python 3.12+

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

print_info() {
    echo -e "${CYAN}[i]${NC} $1"
}

echo -e "${GREEN}"
echo "╔════════════════════════════════════════════════════════════╗"
echo "║     🔍 Termux Smart Search Scraper - Installation        ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Check if running in Termux
if [[ -d "/data/data/com.termux" ]]; then
    print_info "Terdeteksi: Termux Environment"
    IS_TERMUX=true
else
    print_info "Terdeteksi: Non-Termux Environment"
    IS_TERMUX=false
fi

# Step 1: Update package lists
print_info "[1/5] Memperbarui daftar paket..."
if command -v pkg &> /dev/null; then
    pkg update -y > /dev/null 2>&1
    print_status "Package list updated"
else
    print_info "pkg tidak ditemukan, melewati..."
fi

# Step 2: Install system dependencies
print_info "[2/5] Menginstal dependensi sistem..."
if command -v pkg &> /dev/null; then
    pkg install -y python python-pip git libxml2 libxslt > /dev/null 2>&1
    print_status "System dependencies installed"
else
    print_info "Pastikan Python 3 dan Git sudah terinstal"
fi

# Step 3: Setup storage (Termux only)
if [[ "$IS_TERMUX" == true ]]; then
    print_info "[3/5] Mengatur akses penyimpanan..."
    termux-setup-storage 2>/dev/null
    print_status "Storage access configured"
else
    print_info "[3/5] Melewati storage setup (bukan Termux)"
fi

# Step 4: Install Python packages
print_info "[4/5] Menginstal paket Python..."

# Detect pip method
if pip --version &> /dev/null; then
    # Check Python version for PEP 668 compatibility
    PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null || python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    print_info "Python version: $PYTHON_VERSION"
    
    # Try different installation methods
    if pip install -r requirements.txt > /dev/null 2>&1; then
        print_status "Python packages installed (method 1)"
    elif pip install --break-system-packages -r requirements.txt > /dev/null 2>&1; then
        print_status "Python packages installed (method 2: --break-system-packages)"
    elif pip install --user -r requirements.txt > /dev/null 2>&1; then
        print_status "Python packages installed (method 3: --user)"
    else
        print_error "Gagal menginstal paket Python"
        print_info "Coba jalankan manual: pip install --break-system-packages -r requirements.txt"
        exit 1
    fi
else
    print_error "pip tidak ditemukan!"
    print_info "Instal dengan: pkg install python-pip"
    exit 1
fi

# Step 5: Create results directory
print_info "[5/5] Membuat direktori hasil..."
mkdir -p hasil_search
print_status "Directory 'hasil_search' created"

# Verify installation
print_info "\nMemverifikasi instalasi..."

ERRORS=0

# Check Python
if command -v python &> /dev/null || command -v python3 &> /dev/null; then
    print_status "Python: OK"
else
    print_error "Python: NOT FOUND"
    ERRORS=$((ERRORS + 1))
fi

# Check required packages (new packages)
for pkg_name in httpx bs4 duckduckgo_search; do
    if python3 -c "import $pkg_name" 2>/dev/null || python -c "import $pkg_name" 2>/dev/null; then
        print_status "$pkg_name: OK"
    else
        print_error "$pkg_name: NOT FOUND"
        ERRORS=$((ERRORS + 1))
    fi
done

# Final message
echo ""
if [[ $ERRORS -eq 0 ]]; then
    echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║           ✅ INSTALASI BERHASIL!                          ║${NC}"
    echo -e "${GREEN}╚════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${CYAN}Jalankan scraper dengan:${NC}"
    echo -e "  ${GREEN}python main.py${NC}"
    echo ""
else
    echo -e "${YELLOW}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${YELLOW}║  ⚠️  INSTALASI SELESAI DENGAN PERINGATAN                  ║${NC}"
    echo -e "${YELLOW}╚════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${CYAN}Ada $ERRORS masalah. Coba:${NC}"
    echo -e "  ${YELLOW}pip install --break-system-packages -r requirements.txt${NC}"
    echo ""
fi
