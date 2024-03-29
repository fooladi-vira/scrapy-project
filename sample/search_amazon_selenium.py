from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
url='https://www.amazon.com/'
driver.get(url)
driver.maximize_window()
search_box=driver.find_element(By.NAME,'field-keywords')
search_box.send_keys('laptop'+Keys.ENTER)
# time.sleep(2)
# search_icon=driver.find_element(By.ID,'nav-search-submit-button')
# search_icon.click()
time.sleep(2)
prices=driver.find_elements(By.CLASS_NAME,'a-price-whole')

data=[]
for price in prices:
    data.append(price.text)
    
print(data)


