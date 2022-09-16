from selenium import webdriver
import os
import json
 
def browser_initial():
    """"
    浏览器初始化,并打开大麦网购票界面（未登录状态）
    """
    os.chdir('/Cookie')
    browser = webdriver.Chrome()
    browser.get('https://detail.damai.cn/item.htm?spm=a2oeg.search_category.0.0.8778f91as7xLdc&id=610870234751&clicktitle=2020%E5%BC%A0%E6%9D%B0%E3%80%8C%E6%9C%AA%C2%B7LIVE%E3%80%8D%E5%B7%A1%E5%9B%9E%E6%BC%94%E5%94%B1%E4%BC%9A%20%E5%90%88%E8%82%A5%E7%AB%99')
    return browser
 
def log_damai(browser):
    """
    从本地读取cookies并刷新页面,成为已登录状态
    """
    with open('damai_cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
 

    for cookie in listCookies:
        cookie_dict = {
            'domain': '.damai.cn',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            "expires": '',
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False
        }
        browser.add_cookie(cookie_dict)
    browser.refresh()                      # 刷新网页,cookies才成功
    
if __name__ == "__main__":
    browser = browser_initial()
    log_damai(browser)
