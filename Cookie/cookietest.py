#Cookie:
#_xsrf=2|afbcd15d|0f781361e4e5b11395ecedd4a0e22b9b|1661243806; Access_Token=85363921367f4fb381be51c9b502a550

#selenium
from lib2to3.pgen2 import token
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

#HTTP
import requests
def autologin():
    option = webdriver.ChromeOptions()
    # option.add_experimental_option("detach", True)
    option.add_argument('ignore-certificate-errors')
    option.add_experimental_option("excludeSwitches",['enable-automation'])
    option.add_argument('headless')
    browser = webdriver.Chrome(ChromeDriverManager().install(),options=option)
    browser.get('https://192.168.9.99:32206/login.html#')
    print("打开Aistation")
    WebDriverWait(browser, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[3]/div[3]/div[3]/form/div[1]/div/div[1]/input")))
    search = browser.find_element(by=By.XPATH,value=("/html/body/div/div[3]/div[3]/div[3]/form/div[1]/div/div[1]/input"))
    search.send_keys('pengjingwei')
    browser.find_element(by=By.XPATH,value=('/html/body/div/div[3]/div[3]/div[3]/form/div[2]/div/div[1]/input')).send_keys('123456a?')
    search.send_keys(Keys.ENTER)
    print("成功登录")
    time.sleep(3)
    
    return browser
    
def get_token(browser):
    cookietemp = browser.get_cookies()
    print("获取到Cookie")
    print("cookie:",cookietemp)
    tokentemp = cookietemp[0]["value"]
    # print("token:",tokentemp)
    return tokentemp

def open_browser():
    print("开始执行打开Shell任务")
    global start
    start = time.perf_counter()
    option_new = webdriver.ChromeOptions()
    option_new.add_experimental_option("detach", True)
    option_new.add_argument('ignore-certificate-errors')
    
    option_new.add_experimental_option("excludeSwitches",['enable-automation'])
    browser_new = webdriver.Chrome(options=option_new)
    browser_new.minimize_window()
    return browser_new

def addcookie(browser_new,tokentemp):
    cookie_dict = {
            'domain': '192.168.9.99',
            # 'httpOnly': 'False',
            'name': 'Access_Token',
            # 'path': '/',
            # 'Secure': False,
            'value':tokentemp
        }
    browser_new.get("https://192.168.9.99:32206/login.html#")
    print("开始添加Cookie")
    browser_new.add_cookie(cookie_dict)
    browser_new.refresh()
    print("打开shell")
    
    browser_new.get("https://192.168.9.99:32206/index.html#/developEnv/da2f4440-fe5e-48c0-b348-ef87c819e392/info?name=20220829112522&startTime=1661928829000")
    browser_new.maximize_window()
    WebDriverWait(browser_new, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, '/html/body/section/section/section/div[2]/div[1]/div/main/div/div[1]/div[2]/div[1]/div/div/div/div[2]')))
    
    browser_new.find_element(by=By.XPATH,value=('/html/body/section/section/section/div[2]/div[1]/div/main/div/div[1]/div[2]/div[1]/div/div/div/div[2]')).click()
    global end
    end = time.perf_counter()

# def save_cookies():
#     """
#     获取cookies保存至本地
#     """
    
#     dictCookies = browser.get_cookies()    # 获取list的cookies
#     jsonCookies = json.dumps(dictCookies) #  转换成字符串保存
    
#     with open('aistation_cookies.txt', 'w') as f:
#         f.write(jsonCookies)
    # print('cookies保存成功!')
 
# if __name__ == "__main__":
#     tur = browser_initial()
#     get_cookies(tur[0], tur[1])

browser = autologin()
tokentemp = get_token(browser)
browser_new = open_browser()
addcookie(browser_new,tokentemp)
timeuse = end-start
print("time:",timeuse)

headers = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection':'keep-alive',
    'Cookie': 'Access_Token=855aa6d5a1eb4c13ac574b153e9b3e9d',
    'Host': '192.168.9.99:32206',
    'Referer': 'https://192.168.9.99:32206/index.html',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63',
    'X-Accept-Language': 'zh_CN',
    'X-Auth-Token': tokentemp,
}
 


#HTTP Response
url = 'https://192.168.9.99:32206/api/ibase/v1/login'
s = requests.session()
response = s.get(url=url, headers=headers,verify=False)
html = response.text
print("响应：",html)


# bro = webbrowser.open("https://192.168.9.99:32206/index.html#/developEnv?__=1661752098650")