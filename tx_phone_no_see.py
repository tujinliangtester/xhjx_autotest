from appium import webdriver
import unittest
from time import sleep


class phone_no_test(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'#my phone huawei
        desired_caps['deviceName'] = '7N2XEE1588055873'#my phone huawei
        # desired_caps['platformVersion'] = '5.1'  # testing phone oppo
        # desired_caps['deviceName'] = 'LRLNAMTGBI6HBIUK'#testing phone oppo
        desired_caps['appPackage']='com.tencent.mm'
        desired_caps['appActivity']='.ui.LauncherUI'
        desired_caps['noReset']='true'

        desired_caps['chromeOptions']={'androidProcess': 'com.tencent.mm:tools'}

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(10)

    def test(self):
        el=self.driver.find_element_by_id('com.tencent.mm:id/awt')
        el.click()

        el=self.driver.find_element_by_id('com.tencent.mm:id/a94')
        el.click()

        el=self.driver.find_element_by_id('com.tencent.mm:id/b7')
        el.click()

        for context in self.driver.contexts:
            print(context)

if __name__=='__main__':
    suit=unittest.TestLoader.loadTestsFromTestCase(phone_no_test)
    unittest.TextTestRunner.run(suit)