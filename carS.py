from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv

url_base = 'https://www.carsemsar.com/en/qatar/search?page='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

all_cars = []
page = 1
max_pages = 1000

def extract_card_data(card):
    """Extract specific fields from a vehicle card"""
    ul = card.find('ul', class_='listing-details')
    list_items = ul.find_all('li')

    data = {}
    for li in list_items:
        label = li.find('span', class_='field-label')
        value = li.find('span', class_='field-value')

        if label and value:
            key = label.text.strip().replace(':', '')
            val = value.text.strip()
            data[key] = val

    return {
        'Model': card.find('h3', class_='listing-title').text.strip(),
        'KM': data.get('KM Driven', 'N/A'),
        'Dealer': data.get('Dealer', 'N/A'),
        'Update-Date': data.get('Updated', 'N/A'),
        'Price': data.get('Price', 'N/A'),
    }


while page <= 7:
    print(f"Scraping page {page}...")
    
    url = f"{url_base}{page}"
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Got status code {response.status_code}")
        break
    
    soup = BeautifulSoup(response.text, 'lxml')
    main_container = soup.find('aside', class_="col-lg-6")
    
    if not main_container:
        print("No main container found - reached end")
        break
    
    car_cards = main_container.find_all('div', class_='listing-car status-published')
    
    if not car_cards:
        print(f"No cars found (empty page) exiting...")
        break
            
    else:
        print(f"Found {len(car_cards)} cars")
        for card in car_cards:
            car_data = extract_card_data(card)
            all_cars.append(car_data)
    
    page += 1

print(f"Total cars scraped: {len(all_cars)} from {page-1} pages")

if all_cars:
    df = pd.DataFrame(all_cars)
    df.to_csv('cars.csv', index=False, encoding='utf-8-sig')
    print("Data saved successfully to cars.csv")
else:
    print("No data to write. File not created.")
