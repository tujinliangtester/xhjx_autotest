from selenium import  webdriver
import time
driver=webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
def cms():
    driver.get('http://qa.365bencao.cn/malls/sys/index#')
    el = driver.find_element_by_name('userName')
    el.clear()
    el.send_keys('tujinliang')

    el = driver.find_element_by_name('password')
    el.clear()
    el.send_keys('tujinliang')

    el = driver.find_element_by_id('loginButton')
    el.click()

def wms():
    driver.get('http://qa.365bencao.cn/warehouse/sys/login#')
    el = driver.find_element_by_name('userName')
    el.clear()
    el.send_keys('tjl041602')

    el = driver.find_element_by_name('password')
    el.clear()
    el.send_keys('tjl041602')

    time.sleep(1)
    el = driver.find_element_by_id('loginButton')
    el.click()

    time.sleep(2)
    try:
        driver.switch_to.alert.accept()
    except:
        print('no alert')