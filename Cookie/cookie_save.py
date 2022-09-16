from selenium import webdriver
import os
import time
import json
 
def browser_initial():
    """"
    进行浏览器初始化
    """
    os.chdir('/Cookie')
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    option.add_argument('ignore-certificate-errors')
    option.add_experimental_option("excludeSwitches",['enable-automation'])
    # option.add_argument('headless')
    
    browser = webdriver.Chrome(options=option)
    log_url = 'https://192.168.9.99:32206/login.html#'
    return log_url,browser
 
def get_cookies(log_url,browser):
    """
    获取cookies保存至本地
    """
    browser.get(log_url)
    time.sleep(15)     # 进行扫码
    dictCookies = browser.get_cookies()    # 获取list的cookies
    jsonCookies = json.dumps(dictCookies) #  转换成字符串保存
    
    with open('damai_cookies.txt', 'w') as f:
        f.write(jsonCookies)
    print('cookies保存成功!')
 
if __name__ == "__main__":
    tur = browser_initial()
    get_cookies(tur[0], tur[1])
