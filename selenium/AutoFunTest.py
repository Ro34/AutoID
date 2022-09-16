from lib2to3.pgen2 import driver
import time
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



browser = webdriver.Chrome(ChromeDriverManager().install())
#设置载入网址
browser.get('https://rddata.yijiahe.com/login')
#隐式等待
#确保该元素位于页面上, 并且在尝试与该元素交互之前, 该元素处于可交互状态.
driver.implicitly_wait(0.5)
#查找用户名输入框
search = browser.find_element(by=By.ID,value='ant-input m-b-8')
#输入用户名
search.send_keys('pengjingwei')

#查找密码输入框
search = browser.find_element(by=By.CLASS_NAME,value='ant-input')
#输入密码
search.send_keys('yjh123')
#Enter
search.send_keys(Keys.ENTER)
ActionChains(browser).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
time.sleep(5)