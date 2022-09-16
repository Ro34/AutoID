
from http import cookies
from multiprocessing.sharedctypes import Value
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_token():
    option = webdriver.ChromeOptions()
    # option.add_experimental_option("detach", True)
    option.add_argument('ignore-certificate-errors')
    option.add_experimental_option("excludeSwitches",['enable-automation'])
    
    # option.add_argument('window-size=1920x1080')
    option.add_argument('--start-minimized')
    # option.add_argument('disable-infobars')
    option.add_argument('headless')
    # option.add_argument('no-startup-window') 
    
    browser = webdriver.Chrome(ChromeDriverManager().install(),options=option)
    
    browser.get('https://192.168.9.99:32206/login.html#')
    
    
    # time.sleep(0.5)
    #查找用户名输入框
   
    WebDriverWait(browser, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[3]/div[3]/div[3]/form/div[1]/div/div[1]/input")))
    search = browser.find_element(by=By.XPATH,value=("/html/body/div/div[3]/div[3]/div[3]/form/div[1]/div/div[1]/input"))
    search.send_keys('pengjingwei')

    #输入用户名
    # time.sleep(2)
    #查找密码输入框
    browser.find_element(by=By.XPATH,value=('/html/body/div/div[3]/div[3]/div[3]/form/div[2]/div/div[1]/input')).send_keys('123456a?')
    #输入密码
    # search.send_keys('123456a?')
    #Enter
    search.send_keys(Keys.ENTER)
    time.sleep(3)

    cookiestemp = browser.get_cookies()
    tokentemp = cookiestemp[0]['value']
    # print(type(tokentemp))
    # print(tokentemp)
    return tokentemp

def login():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    option.add_argument('ignore-certificate-errors')
    option.add_experimental_option("excludeSwitches",['enable-automation'])
    
    cookies_dict = {
        'domain':'192.168.9.99',
        'name':'Access_Token',
        'path':'/',
        'httpOnly': False,
        'secure':False,
        'value':tokentemp
    }

    browser = webdriver.Chrome(options=option)
    

    browser.minimize_window()
    browser.get('https://192.168.9.99:32206/login#')
    browser.add_cookie(cookies_dict)
    browser.get('https://192.168.9.99:32206/index.html#/developEnv?__=1663209091438')
    # browser.refresh()
    return browser


def start_shell():
    browser.set_window_size(556,523)
    WebDriverWait(browser, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, '/html/body/section/section/aside/div/ul/li[3]/div')))
    #开发环境按钮
    deviconbutton = browser.find_element(by=By.XPATH,value=('/html/body/section/section/aside/div/ul/li[3]/div'))
    browser.execute_script("arguments[0].scrollIntoView();", deviconbutton)
    deviconbutton.click()
    #容器按钮
    WebDriverWait(browser, 10, 0.1).until(EC.presence_of_element_located((By.XPATH,'/html/body/section/section/section/div[2]/div[1]/div/main/div/div[1]/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div')))
    workplatformidbutton  = browser.find_element(by=By.XPATH,value=('/html/body/section/section/section/div[2]/div[1]/div/main/div/div[1]/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div'))
    browser.execute_script("arguments[0].scrollIntoView();",workplatformidbutton)
    workplatformidbutton.click()
    #Shell按钮
    WebDriverWait(browser, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, '/html/body/section/section/section/div[2]/div[1]/div/main/div/div[1]/div[2]/div[1]/div/div/div/div[2]')))
    shellbutton = browser.find_element(by=By.XPATH,value=('/html/body/section/section/section/div[2]/div[1]/div/main/div/div[1]/div[2]/div[1]/div/div/div/div[2]'))
    browser.execute_script("arguments[0].scrollIntoView();", shellbutton)
    shellbutton.click()

def shell_front():
    browser.maximize_window()

tokentemp = get_token()
browser = login()
start_shell()
time.sleep(5)
shell_front()
