from selenium import webdriver
import time
driver=webdriver.Chrome()
url='https://tracking.post.ir/'
driver.get(url)
driver.maximize_window()
time.sleep(2)
url2='https://iranfso.com/index.php?route=account/order/info&order_id=274640'
driver.get(url2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(1)
driver.close()