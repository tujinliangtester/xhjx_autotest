import os
import glob
import unittest
from time import sleep

from appium import webdriver

PLATFORM_VERSION = '4.4'


class AndroidWebViewTests(unittest.TestCase):

    def setUp(self):
        app = os.path.abspath(
                os.path.join(os.path.dirname(__file__),
                             'E:/tjl个人/study/auto/appium/selendroid-test-app.apk'))
        desired_caps = {
            'app': app,
            'appPackage': 'io.selendroid.testapp',
            'appActivity': '.HomeScreenActivity',
            'platformName': 'Android',
            'platformVersion': PLATFORM_VERSION,
            'deviceName': 'Android Emulator'
        }

        if (PLATFORM_VERSION != '4.4'):
            desired_caps['automationName'] = 'selendroid'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                       desired_caps)

    def test_webview(self):
        if (PLATFORM_VERSION == '4.4'):
            button = self.driver.find_element_by_accessibility_id('buttonStartWebviewCD')
        else:
            button = self.driver.find_element_by_name('buttonStartWebviewCD')
        button.click()
        sleep(3)

        # self.driver.switch_to.context('WEB')

        # input_field = self.driver.find_element_by_accessibility_id('Enter your name here!')
        # input_field=self.driver.find_elements_by_class_name('android.widget.EditText')
        # input_field=self.driver.find_element_by_xpath("//android.widget.view[@content-desc='Prefered Car:')]/../preceding-sibling::view[2]/android.widget.EditText")
        input_field=self.driver.find_element_by_xpath("//*/TableRow[3]/View/View[2]/EditText")
        # input_field=self.driver.find_element_by_accessibility_id("Hello, can you please tell me your name?")

        if input_field is None:
            print("found")
        else:
            print("not found")


        sleep(1)
        # print(input_field.get_attribute())
        # input_field.text=''
        # print(input_)
        # self.driver.press_keycode(29, 28672)  # 29 is the keycode of 'a', 28672 is the keycode of META_CTRL_MASK
        # self.driver.press_keycode(112)  # 112 is the keycode of FORWARD_DEL, of course you can also use 67“
        # webdriver.keyevent(123)
        # for i in range(0, len("Enter your name here!")):
        #     webdriver.keyevent(67)

        # print(input_field.get_attribute('content-desc'))
        # input_field[1].clear()
        self.driver.press_keycode(29, 28672)  # 29 is the keycode of 'a', 28672 is the keycode of META_CTRL_MASK
        self.driver.press_keycode(112)

        input_field.send_keys('Appium User')
        input_field.submit()
        print(1111)

        # test that everything is a-ok
        source = self.driver.page_source
        self.assertNotEqual(-1, source.find('This is my way of saying hello'))
        self.assertNotEqual(-1, source.find('"Appium User"'))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidWebViewTests)
    unittest.TextTestRunner(verbosity=2).run(suite)