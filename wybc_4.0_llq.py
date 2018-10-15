
import os
from time import sleep
import unittest
# from selenium import webdriver
# import selenium
from appium import webdriver
# import appium


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = '7N2XEE1588055873'
# desired_caps['app'] = ''
# desired_caps['appPackage'] = 'com.tencent.mm'
# desired_caps['appActivity']='com.tencent.mm.ui.LauncherUI'
# desired_caps['appPackage'] = 'com.quark.browser'
# desired_caps['appActivity']='com.ucpro.BrowserActivity'
# desired_caps['appActivity'] = 'com.tencent.mm.plugin.webview.ui.tools.WebViewUI'
# desired_caps['browserName'] = 'Browser'
# desired_caps['fullReset']='false'
# desired_caps['fastReset']='false'
# desired_caps['noReset']='true'

desired_caps['appPackage']='com.oupeng.mini.android'
# desired_caps['appActivity']='com.opera.android.OperaMainActivity'
desired_caps['appActivity']='com.opera.android.OperaStartActivity'#浏览器启动activity

# desired_caps['appPackage']=' com.tencent.mtt'

# desired_caps['appActivity']='.MainActivity'
# desired_caps['appWaitActivity']='.Settings'

# desired_caps['autoGrantPermissions']=true

# options=selenium.webdriver.ChromeOptions()
# options.add_experimental_option("androidProcess", "com.tencent.mm:tools")
# # capability.setCapability(ChromeOptions.CAPABILITY, options)
# desired_caps['ChromeOptions.CAPABILITY'] =options
# desired_caps['ChromeOptions'] ={'androidProcess': 'com.tencent.mm:tools'}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.implicitly_wait(20)
sleep(10)
print(1)

# driver.switch_to.context('WEBVIEW')
# driver.get('http://qaservice.365bencao.cn/#tabbar-with-shop')
# driver.get()
# el=driver.find_element_by_id('com.oupeng.mini.android:id/start_page_url_layout')
# el.send_keys('baidu')
driver.get('http://www.baidu.com')
driver.implicitly_wait(20)

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
# el=driver.find_element_by_id('com.tencent.mm:id/aoj')
# print(el.text)
# el.click()
#
# el=driver.find_element_by_id('com.tencent.mm:id/aol')
# print(el.text)
# el.click()
#
# # el=driver.find_element_by_xpath('//*[@]')
# sleep(10)
# el=driver.find_element_by_xpath('//*[@src="/static/images/minishop/s1.png"]')
# el.click()



# driver.get('http://qaservice.365bencao.cn/cms/#/cmsHome')
# el=driver.find_element_by_id('com.tencent.mm:id/aoj')
# driver.implicitly_wait(10)
# el.click()
#
# el=driver.find_element_by_id('com.tencent.mm:id/j1')
#
# el.click()

print('2')
sleep(10)
i=0
# try:
#     while i<50:
#
#         print(driver.context(i))
#
#         i+=1
# except:
#     print('tryend')

# driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
#
# print('swich to')
# el=driver.find_element_by_xpath('//img[@src="/static/images/minishop/s1.png"]')
#
# print('buy')
# el.click()

#
# el=driver.find_element_by_tag_name('文件传输助手')
# el.click()

