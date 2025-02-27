import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from dotenv import load_dotenv, find_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

chromedriver_path = os.getenv("CHROME_PATH")
privateProperty_webdriver = webdriver.Chrome()
google_form = os.getenv("GOOGLE_FORM")
property_site = os.getenv("RENT_PROPERTY")
privateProperty_webdriver.get(f"{property_site}")
privateProperty_webdriver.maximize_window()

location_search = privateProperty_webdriver.find_element(By.XPATH, '//*[@id="search-bar-container"]/div/div[1]/div/input')
location_search.send_keys('soweto')
search_result = WebDriverWait(privateProperty_webdriver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="search-bar-container"]/div/div[2]/div/ul/li[2]/button'))
)
search_result.click()
privateProperty_webdriver.implicitly_wait(2)

# Scrap information on the website
page_source = privateProperty_webdriver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

properties = soup.find_all('a', class_='listing-result')
property_details = []

for property in properties:
    price = property.find('div', class_='txt-heading-2').text
    bedrooms = property.find('div', class_='txt-base-regular').text
    location = property.find('span', class_='listing-result__desktop-suburb').text
    address = property.find('span', class_='listing-result__address').text
    available_from = property.find('span', class_='listing-result__badge--available-from').text
    description = property.find('div', class_='listing-result__description').text

    property_dict = {
        'address': str(address),
        'price': str(price.replace('\\xa', '')),
        'location': str(location),
        'bedrooms': str(bedrooms),
        'description': str(description),
        'available_from': str(available_from),
    }

    property_details.append(property_dict)

print(property_details)
# Go to google form and enter information found from the property website
# open a new tab and switch to tab
privateProperty_webdriver.execute_script("window.open('');")
privateProperty_webdriver.switch_to.window(privateProperty_webdriver.window_handles[1])


# enter the google form
privateProperty_webdriver.get(google_form)
privateProperty_webdriver.implicitly_wait(5)

# input property details to google form
# Wait until all input elements are visible and enabled
user_inputs = WebDriverWait(privateProperty_webdriver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'input.whsOnd[jsname="YPqjbf"]'))
)

# Iterate through the input elements and ensure they are visible and interactable
for property in property_details:
    user_inputs = WebDriverWait(privateProperty_webdriver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input.whsOnd[jsname="YPqjbf"]'))
    )

    user_inputs[0].send_keys(property['price'])
    user_inputs[1].send_keys(property['location'])
    user_inputs[2].send_keys(property['bedrooms'])
    user_inputs[3].send_keys(property['description'])
    user_inputs[4].send_keys(property['available_from'])

    submit = privateProperty_webdriver.find_element(By.CSS_SELECTOR, 'span.l4V7wb:nth-child(2)')
    submit.click()

time.sleep(10)
