from initial import appium_init
import time
from selenium.webdriver.support.select import Select
driver=appium_init.driver
#wo de
el=driver.find_element_by_xpath('//*[@title="我的"]')
el.click()

el=driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[2]/div[2]/div[1]')
el.click()

time.sleep(0.5)
driver.switch_to.context('NATIVE_APP')
print('switch to native')
print(driver.current_context)
dx=184/378
dy=130/814
x=driver.get_window_size()['width']*dx
y=driver.get_window_size()['height']*dy
driver.tap(x=x,y=y)

driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
print('switch to web')
print(driver.current_context)


el=driver.find_element_by_class_name('order-info')
print('............................')
print(el.text)