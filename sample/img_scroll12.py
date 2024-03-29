
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import random

driver=webdriver.Chrome()
url='https://torob.com/'
driver.get(url)
driver.maximize_window()

wait=WebDriverWait(driver,10)
search_box=wait.until(EC.element_to_be_clickable((By.ID,'search-query-input')))
search_box.send_keys('laptop'+Keys.ENTER)
time.sleep(3)
end_of_scroll=driver.execute_script('return document.body.scrollHeight')
posts=[]
while True:
    d=driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(5)
    my_scroll=driver.execute_script('return document.body.scrollHeight')
    if my_scroll==end_of_scroll:
        break
    end_of_scroll=my_scroll

images=driver.find_elements(By.CSS_SELECTOR,'div.jsx-2514672dc9197d80 img')


for img in images:
    #print(img.get_attribute('src'))
    post=img.get_attribute('src')
    posts.append(post)

for pic in posts:
        name=random.randrange(1,200)
        with requests.get(pic,stream=True) as r:
            with open (str(name)+'.jpg','wb') as file:
                for pack in r.iter_content(chunk_size=1024):
                    file.write(pack)

        

