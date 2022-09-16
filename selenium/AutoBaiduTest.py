import time
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.baidu.com')
time.sleep(1)
search = browser.find_element(by=By.ID,value='kw')
search.send_keys('时间')
# search = browser.find_element(by=By.ID,value='password')
# search.send_keys('Abc789456123')
search.send_keys(Keys.ENTER)
time.sleep(3)