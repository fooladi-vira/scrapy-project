from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time


from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome()
url='https://www.digikala.com/search/category-notebook-netbook-ultrabook/'
driver.get(url)
driver.maximize_window()
end_of_scroll=driver.execute_script('return document.body.scollHeight')
wait=WebDriverWait(driver,10)
time.sleep(2)
search_box=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.ellipsis.bg-100.grow-1.radius.px-2.px-4-lg.text-body-2 ')))
time.sleep(2)
search_box.send_keys('laptop')




element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="base_layout_desktop_fixed_header"]')))
ActionChains(driver).move_to_element(element).click().perform()