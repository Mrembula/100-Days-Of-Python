from selenium import webdriver
import os
import time
from dotenv import load_dotenv, find_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

chromedriver_path = os.getenv("CHROME_PATH")
linkedin_driver = webdriver.Chrome()
my_email = os.getenv("MY_EMAIL")
linkedIn_password = os.getenv("LINKEDIN")

linkedin_driver.get('https://www.linkedin.com')
linkedin_driver.implicitly_wait(2)

login = linkedin_driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/a')
login.click()

# Insert user information for login
username_login = linkedin_driver.find_element(By.XPATH, '//*[@id="username"]')
username_login.send_keys(my_email)
password_login = linkedin_driver.find_element(By.XPATH, '//*[@id="password"]')
password_login.send_keys(linkedIn_password)
login_button = linkedin_driver.find_element(By.CSS_SELECTOR, '.btn__primary--large')
login_button.click()

# Search for post (job application)
job_post = linkedin_driver.find_element(By.CSS_SELECTOR, '#global-nav > div > nav > ul > li:nth-child(3)')
job_post.click()

time.sleep(3)
title_search = linkedin_driver.find_element(By.TAG_NAME, 'input')
title_search.send_keys("Python")
region_search = linkedin_driver.find_elements(By.TAG_NAME, 'input')[3]
region_search.clear()
region_search.send_keys('South Africa')
submit_search = linkedin_driver.find_element(By.XPATH, '//*[@id="global-nav-search"]/div/div[2]/button[1]')
region_search.send_keys(Keys.RETURN)

# apply for job using easy apply
time.sleep(3)
get_buttons = linkedin_driver.find_elements(By.TAG_NAME, 'button')
for button in get_buttons:
    if not button.is_displayed():
        class_name = button.get_attribute('class')
        print(class_name)
# The apply button isn't available on python but visible on the page. It's too deep too find
# apply_button = linkedin_driver.find_element(By.CLASS_NAME, 'jobs-apply-button artdeco-button artdeco-button--icon-right artdeco-button--3 artdeco-button--primary ember-view')
# easy_apply = WebDriverWait(linkedin_driver, 20).until(EC.element_to_be_clickable((By.ID, 'ember851')))
# easy_apply.click()
# Error code on top use class_name to print every button class and copy. Chck the button you need
time.sleep(1000)
