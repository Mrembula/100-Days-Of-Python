import os
import selenium
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import find_dotenv, load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
get_path = os.getenv('CHROME_PATH')
get_username = os.getenv('X_USERNAME')
get_password = os.getenv('X_PASS')


class InternetSpeedTwitterBot(selenium.webdriver.Chrome,
                              webdriver.ChromeOptions):
    def __init__(self):
        super().__init__()
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.website = webdriver.Chrome(service=Service(get_path), options=self.options)

    def tweet_at_provider(self, text: str):
        self.website.get('https://twitter.com/?lang=en')
        sleep(3)
        self.website.find_element(By.XPATH, '//a[@href="/login"]').click()
        sleep(3)
        self.website.find_element(By.CSS_SELECTOR, 'label.css-175oi2r').click()
        self.website.find_element(By.CSS_SELECTOR, 'label.css-175oi2r').send_keys(get_username)
        sleep(3)
        self.website.find_element(By.XPATH, '//span[text()="Next"]').click()
        sleep(3)
        self.website.find_element(By.XPATH, '//input[@name="password"]').send_keys(get_password)
        self.website.find_element(By.XPATH, '//span[text()="Log in"]').click()
        sleep(7)
        input_text = self.website.find_element(By.CLASS_NAME, 'public-DraftEditorPlaceholder-inner')
        # input_text.click()
        input_text.send_keys(text)

    def get_internet_speed(self):
        self.website.get('https://www.speedtest.net/')
        sleep(3)
        wait = WebDriverWait(self.website, 10)
        self.website.find_element(By.XPATH, '//span[text()="Go"]').click()
        sleep(20)
        download = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'download-speed'))).get_attribute("innerHTML")
        sleep(20)
        upload = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'upload-speed'))).get_attribute("innerHTML")
        return [download, upload]

# <div class="public-DraftEditorPlaceholder-inner" id="placeholder-d74im" style="white-space: pre-wrap;">What is happening?!</div>