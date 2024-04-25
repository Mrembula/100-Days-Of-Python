from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.binary_location = 'C:/Users/Tebog/PycharmProjects/chrome-win64/chrome.exe'
driver_web = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=chrome_options)

driver_web.get('https://www.python.org/')

time_elements = driver_web.find_elements(By.CSS_SELECTOR, 'time')
event_elements = driver_web.find_elements(By.CSS_SELECTOR, '.event-widget li a')


event_time = []
for element in time_elements:
    inner_html_text = driver_web.execute_script("return arguments[0].innerHTML;", element)
    event_time.append(inner_html_text.replace('<span class="say-no-more">', '').replace('</span>', ''))


place_event = [event.get_attribute('innerHTML') for event in event_elements]

events = {}
for i in range(len(place_event)):
    events[i] = {
        'time': event_time[i],
        'name': place_event[i]
    }

print(events)
driver_web.close()
