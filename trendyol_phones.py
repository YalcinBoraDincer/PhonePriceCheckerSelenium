from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time


def fetch_trendyol_phones():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get('https://www.trendyol.com/akilli-cep-telefonu-x-c109460')

    product_names = set()
    prices = []
    SCROLL_PAUSE_TIME = 2
    MAX_SCROLLS = 30
    SCROLL_DISTANCE = 1300

    def scroll_down(driver, distance, pause_time):
        driver.execute_script(f"window.scrollBy(0, {distance});")
        time.sleep(pause_time)

    def get_page_height(driver):
        return driver.execute_script("return document.body.scrollHeight")

    def scrape_products(driver):

        product_elements = driver.find_elements(By.CSS_SELECTOR, 'div.p-card-wrppr')
        for element in product_elements:
            title = element.get_attribute('title')
            price_element = element.find_element(By.CSS_SELECTOR, 'div.price-promotion-container .prc-box-dscntd')
            price = price_element.text if price_element else 'N/A'
            if title and price and title not in product_names:
                product_names.add(title)
                prices.append(price)

    last_height = get_page_height(driver)

    for page in range(MAX_SCROLLS):
        print('Scroll', page + 1, 'scraping...')

        scroll_down(driver, SCROLL_DISTANCE, SCROLL_PAUSE_TIME)

        scrape_products(driver)

    print(f"{len(product_names)} ürün bulundu.")

    df = pd.DataFrame({'Product Name': list(product_names), 'Price': prices[:len(product_names)]})
    df.to_excel('trendyol_products.xlsx', index=False)

    driver.quit()

