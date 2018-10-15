import os
from time import sleep
import unittest
from appium import webdriver

class orderTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = '7N2XEE1588055873'
        desired_caps['appPackage']='com.tencent.mm'
        desired_caps['appActivity']='.ui.LauncherUI'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_user_order(self):
        el=self.driver.find_element_by_id('com.tencent.mm:id/aoj[@text="无忧药膳"]')
        # el=self.driver.find_element_by_xpath('//*[@text="搜索或输入网址"]')
        el.click()

        el=self.driver.find_element_by_id('com.oupeng.mini.android:id/url_field')
        el.send_keys('http://qaservice.365bencao.cn/cms/')

        el=self.driver.find_element_by_id('com.oupeng.mini.android:id/action_button')
        el.click()
        # self.driver.switch_to
        # self.driver.get('http://qaservice.365bencao.cn/home')

if __name__=='__main__':
    suit=unittest.TestLoader().loadTestsFromTestCase(orderTest)
    unittest.TextTestRunner().run(suit)