from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time


driver=webdriver.Chrome()
url='https://www.freelancer.com/job/'
driver.get(url)
print(1)
driver.maximize_window()

print(3)

time.sleep(2)
type_search=driver.find_element(By.ID,'searchbox')
type_search.send_keys('python'+Keys.ENTER)
print(4)
time.sleep(3)
result=driver.find_element(By.XPATH,'//*[@id="results"]/li[2]/a[1]').click()

time.sleep(5)
jobs={}
titles=driver.find_elements(By.XPATH,'//*[@id="project-list"]/div[2]/div/div[1]/div[1]/a')
for it in range(1,len(titles)):
    title=driver.find_element(By.XPATH,'//*[@id="project-list"]/div[2]/div/div[1]/div[1]/a').text
    price=driver.find_element(By.XPATH,'//*[@id="project-list"]/div[2]/div/div[1]/div[3]/div').text
    jobs={title:price}
    print(title,price)












