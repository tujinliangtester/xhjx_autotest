from initial import appium_init
import time
from selenium.webdriver.support.select import Select
driver=appium_init.driver
#wo de
el=driver.find_element_by_xpath('//*[@id="app"]/div/footer/div[2]/a[4]')
el.click()

el=driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[2]/div[2]/div[1]')
el.click()

el=driver.find_element_by_android_uiautomator()
time.sleep(0.5)
els=driver.find_elements_by_class_name('list_content')
print(els[0])
els[0].click()
#
# el=driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div')
# # el=driver.find_element_by_class_name('list_content')
# el.click()


el=driver.find_element_by_class_name('order-info')
print('............................')
print(el.text)