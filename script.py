from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

file = open("script.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow (['Id', 'Name', 'Price', 'Specifications', 'Number of Reviews'])

browser_driver = Service("./chromedriver.exe")
scraper = webdriver.Chrome(service=browser_driver)

scraper.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")
accept_cookies = WebDriverWait(scraper, 10).until(EC.element_to_be_clickable((By. CLASS_NAME, "acceptCookies")))
accept_cookies.click()
scraper.find_elements(By. XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div[1]")

unique_id = 1
while True:
    computer_info = scraper.find_elements(By. CLASS_NAME, "thumbnail")

    for thumbnail in computer_info:
        name = thumbnail.find_element(By. CLASS_NAME, "title")
        price = thumbnail.find_element(By. CLASS_NAME, "pull-right")
        specs = thumbnail.find_element(By. CLASS_NAME, "description")
        number_of_reviews = thumbnail.find_element(By. CLASS_NAME, "ratings")
        writer.writerow(
            [unique_id, name.text, price.text, specs.text, number_of_reviews.text])
        unique_id +=1
        
    try: 
        element = scraper.find_element(By.PARTIAL_LINK_TEXT, '›')
        element.click()
    except NoSuchElementException:
        break

file.close()
scraper.quit()