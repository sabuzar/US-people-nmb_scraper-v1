# Multithreaded Selenium Bot for Phone Number Data Scraping

This project uses `Selenium` in a multithreaded Python script to fetch data from a public search API based on phone numbers sourced from an Excel file.

---

##  Features

- Multithreaded scraping using Python's `threading` module
- Headless Chrome for fast execution
- Graceful exception handling and logging
- Stores output in CSV files
- Works with large datasets (tested with 800K+ records)

---

##  Project Structure

project/
│
├── inputfile/
│ └── 800k-FE-Xfers.xlsx # Input Excel file with phone numbers
│
├── outputfiles/
│ └── data1.csv # Output data from each thread
│ └── data2.csv
│ └── ...
│
├── divers/
│ └── chrome-win/chrome.exe # Optional custom Chrome binary
│
├── scrape.py # Main Python script
├── requirements.txt # Python dependencies
└── README.md # You're reading it!


---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/selenium-threaded-scraper.git
cd selenium-threaded-scraper
