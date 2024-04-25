from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

driver_path = 'C:/Users/Tebog/PycharmProjects/chrome-win64/chromedriver.exe'
options = Options()
options.add_experimental_option("detach", True)
tinder_web = webdriver.Chrome(service=Service(driver_path), options=options)
tinder_web.get('https://tinder.com/')


wait = WebDriverWait(tinder_web, 10)
tinder_web.find_element(By.XPATH, "//div[contains(@class, 'lxn9zzn') and contains(text(), 'I accept')]").click()
sleep(2)
tinder_web.find_elements(By.XPATH, "//div[contains(@class, 'lxn9zzn') and contains(text(), 'Log in')]")[1].click()
sleep(3)
facebook_button = tinder_web.find_element(By.XPATH, '//div[contains(text(), "Log in with Facebook")]')
facebook_button.click()
sleep(5)

# The new tinder opens login using gmail or face account selenium on a page
# you'll have to automate facebook or gmail
# the html or css is not on the tinder page. So not available on the page

# tinder_web.switch_to.new_window('window_handle')

finds_inputs = tinder_web.find_elements(By.TAG_NAME, 'input')
email = tinder_web.find_elements(By.XPATH, '//input[@id="email"]')
password = tinder_web.find_elements(By.XPATH, '//input[@id="pass"]')
print(email, password, finds_inputs)
'''
tinder_web.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
tinder_web.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]').click()
tinder_web.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()

for n in range(100):
    sleep(1)
    try:
        print("called")
        like_button = tinder_web.find_element(By.XPATH,
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = tinder_web.find_element(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)
'''