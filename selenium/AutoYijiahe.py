from lib2to3.pgen2 import driver
import time
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options



browser = webdriver.Chrome(ChromeDriverManager().install())
#设置载入网址
browser.get('http://rddata.yijiahe.com/login')
driver.get('http://rddata.yijiahe.com/')
print(driver.title)
time.sleep(1)
#查找用户名输入框
search = browser.find_element(by=By.ID,value='username')
#输入用户名
search.send_keys('ro34abc@gmail.com')
time.sleep(1)
#查找密码输入框
search = browser.find_element(by=By.ID,value='password')
#输入密码
search.send_keys('Abc789456123')
#Enter
search.send_keys(Keys.ENTER)
ActionChains(browser).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
time.sleep(5)