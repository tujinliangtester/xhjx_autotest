
import os
from time import sleep
import unittest
# from selenium import webdriver
# import selenium
from appium import webdriver
# import appium

class orderTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = '7N2XEE1588055873'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    #
    # def tearDown(self):
    #     # self.driver.quit()

    def test_user_order(self):
        self.driver.get('http://www.baidu.com')
        el=self.driver.find_element_by_android_uiautomator('text("")')

if __name__=='__main__':
    suit=unittest.TestLoader().loadTestsFromTestCase(orderTest)
    unittest.TextTestRunner().run(suit)