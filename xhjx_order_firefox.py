
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
        desired_caps['appPackage']='com.qihoo.browser'
        desired_caps['appActivity']='.launcher.LauncherActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    #
    # def tearDown(self):
    #     # self.driver.quit()

    def test_user_order(self):



        # self.driver.get('http://www.baidu.com')
        # # print(1)
        # el=self.driver.find_element_by_class_name('android.widget.LinearLayout')
        # el.click()
        # print(self.driver.context)
        # el=self.driver.find_element_by_class_name('android.view.View')
        # el.send_keys('http://www.baidu.com')
        # # self.driver.get('http://www.baidu.com')
        # el=self.driver.find_element_by_class_name('android.widget.TextView')
        # el.click()
        el=self.driver.find_element_by_id('com.qihoo.browser.browser:id/b_q')
        el.click()

        el=self.driver.find_element_by_id('com.qihoo.browser.browser:id/a41')
        el.send_keys('http://qaservice.365bencao.cn')

        el=self.driver.find_element_by_id('com.qihoo.browser.browser:id/b09')
        el.click()

        #
        # sleep(5)
        # el=self.driver.find_element_by_class_name('iconfont.icon-sousuo.sercher')
        # el.click()
        sleep(3)
        # el=self.driver.find_element_by_id('com.qihoo.browser.browser:id/b8s')
        # el.click()

        contexts = self.driver.contexts

        for cotext in contexts:
            print(cotext)

        self.driver.switch_to.context(contexts[-1])


if __name__=='__main__':
    suit=unittest.TestLoader().loadTestsFromTestCase(orderTest)
    unittest.TextTestRunner().run(suit)