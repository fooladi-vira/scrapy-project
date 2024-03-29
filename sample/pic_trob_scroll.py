
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver=webdriver.Chrome()
url='https://torob.com/'
driver.get(url)
driver.maximize_window()

wait=WebDriverWait(driver,10)
search_box=wait.until(EC.element_to_be_clickable((By.ID,'search-query-input')))
search_box.send_keys('laptop'+Keys.ENTER)
time.sleep(3)
end_of_scroll=driver.execute_script('return document.body.scrollHeight')
while True:
    d=driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(5)
    my_scroll=driver.execute_script('return document.body.scrollHeight')
    if my_scroll==end_of_scroll:
        break
    end_of_scroll=my_scroll

prices=driver.find_elements(By.CSS_SELECTOR,'.jsx-2514672dc9197d80.product-price-text')
data=[]
i=0
for price in prices:
    data.append(price.text)
    i+=1
    print(str(i)+'    '+price.text)



