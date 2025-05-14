import csv
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

# Input/output files
input_file = 'Ladies_tailor_shops_ranchi_link_basic1.csv'
output_file = 'ladies__tailor_shops_detailed.csv'

with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    shop_links = list(reader)

detailed_data = []

for index, shop in enumerate(shop_links):
    print(f"\n⏳ Processing {index+1}/{len(shop_links)}: {shop['Name']}")
    driver.get(shop['Link'])
    
    # Wait randomly between 5–8 seconds to simulate human browsing
    time.sleep(random.uniform(5, 8))
    
    try:
        full_name = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'DUwDvf'))).text
    except:
        full_name = ''

    try:
        address = driver.find_element(By.XPATH, "//button[@data-item-id='address']").text
    except:
        address = ''

    try:
        phone_button = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[contains(@aria-label, 'Phone') or contains(@data-item-id, 'phone')]")
        ))
        phone = phone_button.text
    except:
        phone = ''

    try:
        website_element = driver.find_element(By.XPATH, "//a[@data-item-id='authority']")
        website = website_element.get_attribute('href')
    except:
        website = ''

    try:
        rating = driver.find_element(By.CLASS_NAME, 'MW4etd').text
        review_count = driver.find_element(By.CLASS_NAME, 'UY7F9').text
    except:
        rating = ''
        review_count = ''

    detailed_data.append({
        'Name': full_name,
        'Link': shop['Link'],
        'Address': address,
        'Phone': phone,
        'Website': website,
        'Rating': rating,
        'Review Count': review_count
    })

    # Every 10 shops, take a longer break (simulate browsing or resting)
    if (index + 1) % 10 == 0:
        print("💤 Taking a long rest...")
        time.sleep(random.uniform(15, 30))

# Save results
keys = detailed_data[0].keys()
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, keys)
    writer.writeheader()
    writer.writerows(detailed_data)

print("\n✅ Done! Data saved to 'ladies_tailor_shops_data.csv'.")
driver.quit()
