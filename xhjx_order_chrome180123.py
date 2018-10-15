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
        desired_caps['browserName'] = 'Browser'
        # desired_caps['platformVersion'] = '4.4'#my phone huawei
        # desired_caps['deviceName'] = '7N2XEE1588055873'#my phone huawei

        desired_caps['platformVersion'] = '5.1'  # testing phone oppo
        desired_caps['deviceName'] = 'LRLNAMTGBI6HBIUK'#testing phone oppo
        # desired_caps['appPackage']='com.tencent.mm'
        # desired_caps['appActivity']='.ui.LauncherUI'
        desired_caps['noReset']='true'

        # desired_caps['chromeOptions']={'androidProcess': 'com.tencent.mm:tools'}

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(10)
    #
    # def tearDown(self):
    #     self.driver.quit()

    def test_user_order(self):
        # el = self.driver.find_element_by_id('com.tencent.mm:id/aoh')#huawei
        self.driver.get('www.baidu.com')



if __name__=='__main__':
    suit=unittest.TestLoader().loadTestsFromTestCase(orderTest)
    unittest.TextTestRunner().run(suit)