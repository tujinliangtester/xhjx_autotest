from selenium import  webdriver
import time
driver=webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
# driver.minimize_window()
def cms():
    time.sleep(0.5)
    driver.get('http://qa.365bencao.cn/malls/sys/index#')
    time.sleep(1)
    el = driver.find_element_by_name('userName')
    el.clear()
    el.send_keys('tujinliang')

    el = driver.find_element_by_name('password')
    el.clear()
    el.send_keys('tujinliang')

    el = driver.find_element_by_id('loginButton')
    el.click()

def wms():
    time.sleep(0.5)
    driver.get('http://qa.365bencao.cn/warehouse/sys/login#')
    time.sleep(1)
    el = driver.find_element_by_name('userName')
    el.clear()
    el.send_keys('tjl041602')

    time.sleep(0.5)
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