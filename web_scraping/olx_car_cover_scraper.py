from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv

# Setup Selenium
options = Options()
options.add_argument("--headless")  # Run headless (invisible browser)
driver = webdriver.Chrome(options=options)

# Load the OLX search page
url = "https://www.olx.in/items/q-car-cover"
driver.get(url)
time.sleep(5)  # Wait for JavaScript to load results

# Scrape the data
results = []

# Find listings
ads = driver.find_elements(By.CSS_SELECTOR, 'li.EIR5N')

for ad in ads:
    try:
        title = ad.find_element(By.CSS_SELECTOR, 'span._2tW1I').text
        price = ad.find_element(By.CSS_SELECTOR, 'span._89yzn').text
        link = ad.find_element(By.TAG_NAME, 'a').get_attribute('href')
        results.append([title, price, link])
    except Exception as e:
        continue  # Skip if any field is missing

driver.quit()

# Save to CSV
with open('olx_car_covers.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Link'])
    writer.writerows(results)

print("Scraped and saved to 'olx_car_covers.csv' successfully!")
