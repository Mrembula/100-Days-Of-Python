import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


url = '/wiki/Special:Statistics'
timeout = 50 # 5 minutes
start_time = time.time()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.binary_location = 'C:/Users/Tebog/PycharmProjects/chrome-win64/chrome.exe'
driver_web = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=chrome_options)

driver_web.get("https://orteil.dashnet.org/experiments/cookie/")

while True:
    click_cookie = driver_web.find_element(By.ID, "cookie")
    if time.time() - start_time <= timeout:
        click_cookie.click()
    else:
        break

time.sleep(30)
driver_web.quit()
