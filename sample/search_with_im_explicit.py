from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()
url='https://www.amazon.com/'
driver.get(url)
#driver.implicitly_wait(10)
driver.maximize_window()
search_box=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,'field-keywords')))
search_box.send_keys('laptop'+Keys.ENTER)

prices=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'a-price-whole')))

data=[]
for price in prices:
    data.append(price.text)
    
print(data)


