from initial import appium_init
import time
from selenium.webdriver.support.select import Select
from tools import common
from appium.webdriver.common.touch_action import TouchAction


driver=appium_init.driver
#wo de
el=driver.find_element_by_xpath('//*[@title="我的"]')
el.click()

el=driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[2]/div[2]/div[1]')
el.click()

dx=460/1080
dy=600/1920
common.click_native(dx=dx,dy=dy)


js="return document.querySelector('.order-info p').innerText"
s=driver.execute_script(js)
print(s)
s=s[5:]
print(s)