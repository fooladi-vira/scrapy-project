from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time


driver=webdriver.Chrome()
url='https://www.amazon.com/'
driver.get(url)
driver.maximize_window()
end_of_scroll=driver.execute_script('return document.body.scrollHeight')
wait=WebDriverWait(driver,10)
search_box=wait.until(EC.element_to_be_clickable((By.NAME,'field-keywords')))
search_box.send_keys('laptop'+Keys.ENTER)
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(3)
    my_scroll=driver.execute_script('return document.body.scrollHeight')
    if my_scroll==end_of_scroll:
        break
    end_of_scroll=my_scroll

prices=wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'a-price-whole')))
data=[]
for price in prices:
    data.append(price.text)
    
print(data)


