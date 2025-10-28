import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

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
                print("No more content to load (button disappeared)")
                break
    cards = driver.find_elements(By.CSS_SELECTOR, "div.v-card-wrapper")
    print(f"\nFound {len(cards)} vehicles\n")
    
    for i, card in enumerate(cards, 1):
        print(f"--- Card {i} ---")
        print(card.text)
        print()

finally:
    time.sleep(5)
    driver.quit()

