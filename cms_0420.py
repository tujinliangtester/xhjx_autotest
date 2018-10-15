from selenium import webdriver
cmsdriver=webdriver.Firefox()

def login():
    #login
    cmsdriver.get('http://qa.365bencao.cn/malls/sys/login')
    el=cmsdriver.find_element_by_name('userName')
    el.send_keys('tujinliang')

    el=cmsdriver.find_element_by_name('password')
    el.send_keys('tujinliang')

    el=cmsdriver.find_element_by_id('loginButton')
    el.click()

def sp():
    el=cmsdriver.find_element_by_xpath('//*[@id="navbar_top"]/li[2]/a')
    el.click()

