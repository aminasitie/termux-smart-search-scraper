#!/bin/bash
# Termux Smart Search Scraper - Installation Script

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Termux Smart Search Scraper - Installation ===${NC}"

# Check if running in Termux
if [[ ! -d "/data/data/com.termux" ]]; then
    echo -e "${YELLOW}Warning: This script is optimized for Termux.${NC}"
    echo -e "${YELLOW}Some features may not work on other systems.${NC}"
fi

# Update package lists
echo -e "\n${GREEN}[1/4] Updating package lists...${NC}"
pkg update -y

# Install Python and dependencies
echo -e "\n${GREEN}[2/4] Installing Python and dependencies...${NC}"
pkg install python python-pip git -y

# Setup storage access (Termux)
echo -e "\n${GREEN}[3/4] Setting up storage access...${NC}"
if [[ -d "/data/data/com.termux" ]]; then
    termux-setup-storage
    echo -e "${YELLOW}Please grant storage permission when prompted.${NC}"
    sleep 2
fi

# Install Python packages
echo -e "\n${GREEN}[4/4] Installing Python packages...${NC}"
pip install --upgrade pip
pip install -r requirements.txt

# Create results directory
echo -e "\n${GREEN}Creating results directory...${NC}"
mkdir -p hasil_search

echo -e "\n${GREEN}=== Installation Complete ===${NC}"
echo -e "${GREEN}Run the scraper with: python main.py${NC}"
