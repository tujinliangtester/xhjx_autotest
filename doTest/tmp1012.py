from initial import appium_init
import time
from selenium.webdriver.support.select import Select
from tools import common


driver=appium_init.driver
#wo de
el=driver.find_element_by_xpath('//*[@title="我的"]')
el.click()

el=driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[2]/div[2]/div[1]')
el.click()

dx=460/1080
dy=600/1920
common.click_native(dx=dx,dy=dy)


el=driver.find_element_by_class_name('order-info')
print('............................')
print(el.text)