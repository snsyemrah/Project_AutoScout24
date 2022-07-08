from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

url="https://www.centraalbeheer.nl/verzekeringen/autoverzekering/kentekencheck" 
driver.get(url)


# # buton=driver.find_element_by_xpath('//*[@id="L2AGLb"]')  #.click()
time.sleep(10)
# driver.find_element(By.CLASS_NAME, "button.accept").click()
# buton=driver.find_element(By.XPATH, '//*[@id="tekst1"]/div[2]/a[1]').click()

