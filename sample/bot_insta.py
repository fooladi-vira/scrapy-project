from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

class Bot:
    def __init__(self,user,password):
        self.driver=webdriver.Chrome()
        self.user=user
        self.password=password
        
        
        
    def Login(self):
        driver=self.driver
        url='https://www.instagram.com/'
        driver.get(url)
        driver.maximize_window()

        element = driver.find_element(By.CSS_SELECTOR,'input[aria-label="Phone number, username, or email"][name="username"]')
        time.sleep(2)
        element.send_keys(self.user)
        
        password=driver.find_element(By.NAME,'password').send_keys(self.password)
        time.sleep(2)
        btn_login=driver.find_element(By.CSS_SELECTOR,'button[type="submit"] ').click()
        time.sleep(2)
        print('you are login successfull')
        
    def like(id_insta,self):
        url='https://www.instagram.com/'+id_insta
        driver=self.driver
        driver.get(url)
        if driver.text:
            print('search ok')
            driver.find_element(By.CLASS_NAME,'_aagw').click()
            like_ele=driver.find_element(By.CLASS_NAME, 'x6s0dn4 x78zum5 xdt5ytf xl56j7k')
            like_btn=driver.find_element(By.XPATH,'//*[contains(aria-label,"Like")]')
            if like_btn :
                time.sleep(2)
                like_btn.click()
                time.sleep(1)
                next=driver.find_element(By.CLASS_NAME,'_abl-').click()
                print('like')
            
            elif driver.find_element(By.XPATH,'//*[contains(aria-label,"UnLike")]'):
                time.sleep(1)
                next=driver.find_element(By.CLASS_NAME,'_abl-').click()
            
        

test=Bot('fooladizeinab','Vira2150_')
id_insta='itviraco'
test.Login()
for i in range(1,5):
    test.like(id_insta)