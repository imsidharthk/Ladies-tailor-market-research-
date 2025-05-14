from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def open_google_maps(driver):
    driver.get("https://www.google.com/maps")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "searchboxinput"))
    )


def search_query(driver, query):
    search_box = driver.find_element(By.ID, "searchboxinput")
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.hfpxzc'))
    )


def scroll_results(driver, scroll_times=20, delay=2):
    for _ in range(scroll_times):
        try:
            scrollable_div = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='feed']"))
            )
            driver.execute_script("arguments[0].scrollTop += 1000;", scrollable_div)
            time.sleep(delay)
        except Exception as e:
            print(" Scrolling error:", e)
            break


def extract_shop_data(driver):
    shops = driver.find_elements(By.CSS_SELECTOR, 'a.hfpxzc')
    shop_data = []

    for index, shop in enumerate(shops):
        name = shop.get_attribute("aria-label")
        link = shop.get_attribute("href")
        if name and link:
            print(f"{index + 1}. {name} --> {link}")
            shop_data.append({"Name": name, "Link": link})

    return pd.DataFrame(shop_data)


def save_to_csv(df, filename="tailor_shops_ranchi_link_basic1.csv"):
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"\n✅ Data saved to '{filename}'")


def main():
    driver = setup_driver()
    try:
        open_google_maps(driver)
        search_query(driver, "tailor shop in Ranchi, Jharkhand")
        scroll_results(driver, scroll_times=20)
        df = extract_shop_data(driver)
        save_to_csv(df)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
