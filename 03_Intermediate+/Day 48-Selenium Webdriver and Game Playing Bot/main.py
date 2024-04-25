from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.binary_location = '../../../chrome-win64/chrome.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

price = driver.find_element(By.ID, 'priceblock ourprice')
by_name = driver.find_element(By.TAG_NAME, 'priceblock ourprice')
by_class = driver.find_element(By.CLASS_NAME, 'priceblock ourprice')
selector = driver.find_element(By.CSS_SELECTOR, 'Your information')
by_path = driver.find_element(By.XPATH, 'do some search on this')

driver.get('https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_3?adgrpid=158527346836&dib=eyJ2IjoiMSJ9.2bTkAlQ1-EFEsdfcFbCM7djkeoOsZU7fq_d646rg5f75oxM8-X-AzkhXdMx8V62zNDFCX0Dcv6-PxlK3eDlt1ib-N7y3Qm_nDV8L4rIs6CuNZb1J4MYM124m2eFJwCEpI30oCAe_Zi_rEo2Prm63hRkGZycKkQe5mWhLpljNKs4eFnoBB7iPmpYG3AMqXLjIJkMZKC59RkP0kYJjez9gxqenegeYOOAkt0u4mQzJoDk._R_8QcTuwy07cCr4T2mjEv9nBhUmEHPAZTAFy7RSxT0&dib_tag=se&gad_source=1&gclid=CjwKCAjw_e2wBhAEEiwAyFFFo_KgGlFSDyyE8E8aP8fG7u_bashWvWPcFPVSFKx1882_3c-svy-UPBoCUq4QAvD_BwE&hvadid=689757507033&hvdev=c&hvlocphy=1029034&hvnetw=g&hvqmt=b&hvrand=15277520036071206745&hvtargid=kwd-361652192637&hydadcr=17669_13650182&keywords=instant%2Bpot%2Bduo%2B7&qid=1713083604&sr=8-3&th=1')
