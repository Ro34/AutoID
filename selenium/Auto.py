

from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

ch_options = Options()
ch_options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=ch_options)
browser = webdriver.Chrome(ChromeDriverManager().install())

def runtest():
    
    #设置载入网址
    browser.get('https://cvat.org/')
    # time.sleep(1)
    #查找用户名输入框
    search = browser.find_element(by=By.ID,value='username')
    #输入用户名
    search.send_keys('ro34abc@gmail.com')
    # time.sleep(1)
    #查找密码输入框
    search = browser.find_element(by=By.ID,value='password')
    #输入密码
    search.send_keys('Abc789456123')
    #Enter
    search.send_keys(Keys.ENTER)
  

runtest()