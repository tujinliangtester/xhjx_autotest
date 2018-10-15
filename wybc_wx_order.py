import os
from time import sleep
import unittest
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class orderTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = '7N2XEE1588055873'
        desired_caps['appPackage']='com.tencent.mm'
        desired_caps['appActivity']='.ui.LauncherUI'
        desired_caps['noReset']='true'

        desired_caps['chromeOptions']={'androidProcess': 'WEBVIEW_com.tencent.mm:tools'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(10)
    #
    # def tearDown(self):
    #     self.driver.quit()

    def test_user_order(self):
        el=self.driver.find_element_by_id('com.tencent.mm:id/aoh')
        # el = self.driver.find_element_by_id('com.tencent.mm:id/apd')#fgc
        # el=self.driver.find_element_by_xpath('//*[@text="搜索或输入网址"]')
        el.click()
        # el.click()
        # i=0
        # while i<5:
        #     el.click()
        #     i+=1
        # sleep(3)

        el=self.driver.find_element_by_id('com.tencent.mm:id/acs')
        # el=self.driver.find_element_by_id('com.tencent.mm:id/ad9')#fgc

        el.click()

        sleep(50)

        # self.driver.switch_to.context('NATIVE_APP')
        # print('switch to NATIVE_APP')

        contexts = self.driver.contexts

        for cotext in contexts:
            print(cotext)

        # el=self.driver.find_element_by_id('com.oupeng.mini.android:id/action_button')
        # el.click()
        # self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT,{"name": "WEBVIEW_com.tencent.mm:tools"})
        self.driver.switch_to.context("WEBVIEW_com.tencent.mm:tools")
        print(self.driver.context)
        # self.driver.switch_to.contexts[3]

        print(1111)
        # self.driver.get('http://qaservice.365bencao.cn/home')

if __name__=='__main__':
    suit=unittest.TestLoader().loadTestsFromTestCase(orderTest)
    unittest.TextTestRunner().run(suit)