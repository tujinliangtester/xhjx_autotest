
import os
from time import sleep
import unittest

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = '7N2XEE1588055873'
# desired_caps['app'] = ''
# desired_caps['appPackage'] = 'com.tencent.mm'
# desired_caps['appActivity']='com.tencent.mm.ui.LauncherUI'
desired_caps['appPackage'] = 'com.quark.browser'
desired_caps['appActivity']='com.ucpro.BrowserActivity'
# desired_caps['appActivity'] = 'com.tencent.mm.plugin.webview.ui.tools.WebViewUI'
# desired_caps['browserName'] = 'Browser'
# desired_caps['fullReset']='false'
# desired_caps['fastReset']='false'
# desired_caps['noReset']='true'

# options = ChromeOptions()
# options.setExperimentalOption("androidProcess", "com.tencent.mm:tools")
# capability.setCapability(ChromeOptions.CAPABILITY, options)

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
sleep(5)
print(1)

# driver.get('http://qaservice.365bencao.cn/#tabbar-with-shop')

# el=driver.find_element_by_id('com.tencent.mm:id/aoj')
# el=driver.find_element_by_accessibility_id('com.tencent.mm:id/c2z')
# el=driver.find_element_by_tag_name('文件传输助手')

# el=driver.find_element_by_xpath('//*[contains(@text,"无忧药膳")]')
# el.click()
#
# el=driver.find_element_by_xpath('//*[@text="我"]')
# el.click()
#
# el=driver.find_element_by_xpath('//*[@text="店铺推广"]')
# el.click()

# el=driver.find_element_by_xpath('//*[@text="店铺推广"]')
# el.click()

# el=driver.find_element_by_xpath('//android.view.View[contains(@text,"文件传输助手")]')
el=driver.find_element_by_id('com.tencent.mm:id/aoj')
print(el.text)
el.click()

el=driver.find_element_by_id('com.tencent.mm:id/aol')
print(el.text)
el.click()

# el=driver.find_element_by_xpath('//*[@]')
sleep(10)
el=driver.find_element_by_xpath('//*[@src="/static/images/minishop/s1.png"]')
el.click()
print('2')
#
# el=driver.find_element_by_tag_name('文件传输助手')
# el.click()

