from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


def fetch_amazon_phones():
    # WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    # Page Amazon/MobilePhones
    driver.get(
        'https://www.amazon.com.tr/s?k=telefon&i=electronics&rh=n%3A13709907031%2Cp_n_feature_twenty-nine_browse-bin%3A44345738031%7C44345740031%7C44345742031%7C44345744031%7C81325702031%7C81325703031%7C81325704031%7C81325705031%7C92070738031&dc&crid=2DBB2GF9MVLV8&qid=1723567235&rnid=44345736031&sprefix=tele%2Caps%2C137&ref=sr_nr_p_n_feature_twenty-nine_browse-bin_7&ds=v1%3A%2FlF4lKhJQxBGwK4RJRFGHqdOOofMA9I7HBWjJnwo%2FFE')

    # Products
    product_names = []
    prices = []

    # First ten pages
    for page in range(10):
        print('Page', page + 1, 'scrapping...')

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-size-base-plus.a-color-base.a-text-normal"))
        )

        # Product Name
        product_elements = driver.find_elements(By.CSS_SELECTOR, "span.a-size-base-plus.a-color-base.a-text-normal")

        # Prices
        price_elements_whole = driver.find_elements(By.CSS_SELECTOR, 'span.a-price-whole')
        price_elements_decimal = driver.find_elements(By.CSS_SELECTOR, 'span.a-price-decimal')

        for i in range(min(len(product_elements), len(price_elements_whole))):
            product_name = product_elements[i].text
            product_names.append(product_name)

            price_whole = price_elements_whole[i].text
            price_decimal = price_elements_decimal[i].text if i < len(price_elements_decimal) else ''
            price = f'{price_whole}{price_decimal}'
            prices.append(price)

        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '.s-pagination-next')
                )
            )
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(2)
        except Exception as e:
            print("There is not next button or its passive:", e)
            break

    print(f"{len(product_names)} ürün bulundu.")

    # Create DataFrame from dictionary
    df = pd.DataFrame({'Product Name': product_names, 'Price': prices})
    df.to_excel('amazon_products.xlsx', index=False)

    driver.quit()
