from appium import webdriver
import time
desired_caps = {
"platformName": "Android",
"platformVersion": "4.4.2",
"deviceName": "7N2XEE1588055873",
"browserName":"Browser"}
print("1")
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
#el=driver.find_element_by_id('com.android.browser:id/url')
#el2=driver.find_element_by_accessibility_id('com.android.browser:id/url')
#el2.send_keys('http://qaservice.365bencao.cn/#tabbar-with-shop')
print("start to get url")
driver.get("http://qaservice.365bencao.cn")
time.sleep(5)
print("start to find element")
el=driver.find_element_by_xpath("//a[contains(@href,'#tabbar-with-shop')]")
el.click()
print("click")
time.sleep(30)
el=driver.find_element_by_name("热卖专区")
el.click()
driver.quit()
