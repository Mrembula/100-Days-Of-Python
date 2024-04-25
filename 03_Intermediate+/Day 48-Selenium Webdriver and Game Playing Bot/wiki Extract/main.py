from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

url = '/wiki/Special:Statistics'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.binary_location = 'C:/Users/Tebog/PycharmProjects/chrome-win64/chrome.exe'
driver_web = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=chrome_options)

driver_web.get('https://en.wikipedia.org/wiki/Main_Page')

english_articles = driver_web.find_element(By.XPATH, f"//a[@href='{url}']")
print(english_articles.get_attribute('innerHTML'))
# english_articles.click()
click_button = driver_web.find_element(By.XPATH, "//a[@href='/wiki/Special:Search']")
click_button.click()
search = driver_web.find_element(By.CLASS_NAME, "cdx-typeahead-search--show-thumbnail")
search.send_keys('Python')
search.send_keys(Keys.ENTER)

# driver_web.quit()
# <div class="cdx-typeahead-search cdx-typeahead-search--show-thumbnail cdx-typeahead-search--auto-expand-width vector-typeahead-search">
