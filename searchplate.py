from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

url="https://www.centraalbeheer.nl/verzekeringen/autoverzekering/kentekencheck" 
driver.get(url)
time.sleep(3)
# Database'den buraya veri alinacak.
kenteken = "86HGDS"
time.sleep(3)

# driver.find_element(By.XPATH, "i//*[@id="tekst1"]/div[2]/a[1]")
# driver.find_element(By.XPATH, '//*[@id="tekst1"]/div[2]/a[1]').click()
# //*[@id="tekst1"]/div[2]/a[1]
time.sleep(3)

kenteken_ = driver.find_element(By.CLASS_NAME, "input-kenteken__input")

kenteken_.send_keys(kenteken)
time.sleep(5)
driver.find_element(By.ID, "kenteken-button").click()

