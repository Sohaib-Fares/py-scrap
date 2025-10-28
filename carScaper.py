import csv
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def extract_card_data(card):
    """Extract specific fields from a vehicle card"""
    overview_items = card.find_elements(By.CSS_SELECTOR, ".v-overview__text")
    prices = card.find_elements(By.CSS_SELECTOR, ".ndfe-current-price")
    
    return {
        'make': card.find_element(By.CSS_SELECTOR, ".make").text,
        'model': card.find_element(By.CSS_SELECTOR, ".model").text,
        'variant': card.find_element(By.CSS_SELECTOR, ".variant").text,
        'status': card.find_element(By.CSS_SELECTOR, ".attention-grabber-text").text,
        'year': overview_items[0].text,
        'transmission': overview_items[1].text,
        'color': overview_items[2].text,
        'fuel_type': overview_items[3].text,
        'monthly_payment': prices[0].text,
        'total_price': prices[1].text,
        'vehicle_id': card.get_attribute('data-vehicle-id'),
        'url': card.find_element(By.CSS_SELECTOR, "a[title]").get_attribute('href')
    }


options = uc.ChromeOptions()
options.binary_location = "/usr/bin/thorium-browser"

driver = uc.Chrome(options=options, version_main=130)

try:
    driver.get("https://www.mercedes-benz-mena.com/qatar/en/buy-new/")
    time.sleep(3)
    
    while True:
        try:
            load_more_content = driver.find_element(By.CSS_SELECTOR, "button.v-load-more-btn")
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", load_more_content)
            time.sleep(3)
            print("Loaded more content...")
        except NoSuchElementException:
            print("No more content to load")
            break
    
    cards = driver.find_elements(By.CSS_SELECTOR, "div.v-card-wrapper")
    print(f"\nFound {len(cards)} vehicles")
    
    vehicles = [extract_card_data(card) for card in cards]

    with open('vehicles.csv', 'w', newline='', encoding='utf-8') as f:
        if vehicles:
            writer = csv.DictWriter(f, fieldnames=vehicles[0].keys())
            writer.writeheader()
            writer.writerows(vehicles)

    print(f"Saved {len(vehicles)} vehicles to vehicles.csv")

finally:
    time.sleep(5)
    driver.quit()