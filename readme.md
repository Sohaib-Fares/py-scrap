# Python Web Scraping - Learning Project

A personal learning project exploring web scraping techniques using Python. This repository contains practice scripts for both dynamic and static web scraping.

## What I'm Learning

This project helps me understand:
- **Dynamic scraping** with Selenium and undetected-chromedriver
- **Static scraping** with BeautifulSoup and requests
- Working with pandas for data manipulation
- Exporting scraped data to CSV format
- Handling different types of web content (dynamic loading, tables)

## Project Contents

- **carScaper.py** - Scrapes Mercedes-Benz Qatar vehicle listings (dynamic content with Selenium)
- **WikiScraper.py** - Scrapes Wikipedia tables (static content with BeautifulSoup)
- **vehicles.csv** - Sample output from the car scraper

## Technologies Used

- Python 3
- Selenium & undetected-chromedriver
- BeautifulSoup4
- Requests
- Pandas

## Quick Start

```bash
# Install dependencies
pip install selenium undetected-chromedriver beautifulsoup4 requests pandas

# Run the scrapers
python carScaper.py
python WikiScraper.py
```

## � Notes

This is a learning project for educational purposes only. Always respect website terms of service and robots.txt when scraping.
