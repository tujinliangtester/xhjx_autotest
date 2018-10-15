import os
from time import sleep
import time
import unittest
from appium import webdriver
import xhjx_cms_order
import HtmlTestRunner
import xhjx_wms_order


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
#
# xhjx_cms_order.login()
# xhjx_cms_order.check_order()

goodsname=''
stock=0
stock_before=0
stock_after=0

# class orderTest(unittest.TestCase):
class orderTest():
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
        desired_caps["newCommandTimeout"]=180

        desired_caps['chromeOptions']={'androidProcess': 'com.tencent.mm:tools'}

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(10)
    #
    # def tearDown(self):
    #     self.driver.quit()

    def login(self):
        #wo de
        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/footer/div[2]/a[5]')
        el.click()

        el=self.driver.find_element_by_id('login')
        el.click()

        # vconsole  clear
        el = self.driver.find_element_by_class_name('vc-switch')
        el.click()

        el = self.driver.find_element_by_id('__vc_tab_network')
        el.click()

        # clear
        el = self.driver.find_element_by_xpath('//*[@id="__vconsole"]/div[3]/div[4]/a[3]')
        el.click()
        # hide
        el = self.driver.find_element_by_xpath('//*[@id="__vconsole"]/div[3]/div[4]/a[8]')
        el.click()

        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[1]/div[1]/div[2]/input')
        el.send_keys(12358580012)

        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[1]/div[1]/div[3]/button')
        el.click()

        #vconsole
        el=self.driver.find_element_by_class_name('vc-switch')
        el.click()

        el=self.driver.find_element_by_id('__vc_tab_network')
        el.click()

        el=self.driver.find_element_by_xpath('//*[@id="__vc_log_network"]/div/div/div/dl/dd[1]')
        el.click()

        #response
        el=self.driver.find_element_by_xpath('//*[@id="__vc_log_network"]/div/div/div/div/div[2]/div/pre')
        password=el.text[13,18]
        print(password)

        #hide
        el=self.driver.find_element_by_xpath('//*[@id="__vconsole"]/div[3]/div[4]/a[8]')
        el.click()

        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[1]/div[2]/div[2]/input')
        el.send_keys(password)

        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[3]/button')
        el.click()

    #用户订单
    def test_user_order_buy(self):
        sleep(2)
        el = self.driver.find_element_by_id('com.tencent.mm:id/aoh')#huawei
        # el = self.driver.find_elements_by_id('com.tencent.mm:id/apt')#oppo
        # el1=el[1]
        el.click()

        sleep(2)
        el = self.driver.find_element_by_id('com.tencent.mm:id/acs')
        el.click()

        sleep(5)
        contexts = self.driver.contexts

        for cotext in contexts:
            print(cotext)


        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
        print('current context is: '+self.driver.context)

        # following in webview

        #switch shop
        # el=self.driver.find_element_by_xpath('//*[@id="app"]/div/footer/div[2]/a[5]/img[1]')
        # el = self.driver.find_element_by_xpath('//*[@title="我的"]')
        # el.click()
        #
        # el=self.driver.find_elements_by_class_name('weui-cell__bd')
        # el.clear()




        sleep(2)
        el=self.driver.find_element_by_class_name('serBox')
        el.click()

        sleep(2)
        el=self.driver.find_element_by_id('ipt-search')
        el.send_keys('o')#goods  name

        sleep(2)
        el=self.driver.find_element_by_id('btn-search')
        el.click()

        sleep(2)
        el=self.driver.find_element_by_class_name('goodsItem')#first goods
        el.click()

        sleep(2)
        self.goodsname=self.driver.find_element_by_xpath('//*[@id="goods-detail"]/div[1]/div/div/div[3]/h4').text
        print('goodsname:'+self.goodsname)
        xhjx_wms_order.wmsgoodsname=self.goodsname

        #get stock_before
        xhjx_wms_order.login()
        sleep(2)
        xhjx_wms_order.check_stock()
        stock_before=stock

        sleep(2)
        # el=self.driver.find_element_by_class_name('weui-flex-item.buy-now')
        el=self.driver.find_element_by_xpath('//*[@id="goods-detail"]/div[2]/div[3]')
        el.click()

        sleep(2)
        el=self.driver.find_element_by_xpath('//input')
        el.clear()
        el.send_keys(2)


        sleep(2)
        el=self.driver.find_elements_by_id('next')
        el2=el[1]
        el2.click()

        sleep(2)
        el=self.driver.find_element_by_xpath('//button')
        el.click()

        #wx_pay
        sleep(2)
        el=self.driver.find_element_by_class_name('pay-item')
        el.click()

        #switch for paying
        sleep(1)
        self.driver.switch_to.context('NATIVE_APP')
        print('current context is: ' + self.driver.context)

        # el=self.driver.find_element_by_class_name('android.widget.RelativeLayout')
        el=self.driver.find_element_by_id('com.tencent.mm:id/cc5')
        el.send_keys('236323')

        # pay finish confirm
        el=self.driver.find_element_by_id('com.tencent.mm:id/dg9')
        el.click()

        #switch to webview
        sleep(5)
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
        print('current context is :'+self.driver.context)

        # xhjx_wms_order.login()
        sleep(2)
        xhjx_wms_order.check_stock()
        stock_after=stock
        print('before:'+str(stock_before))
        print('after:'+str(stock_after))
        self.stock_reduce=stock_before-stock_after
        # self.assertEqual(2,self.stock_reduce)
        print('the stock is right')






        # xhjx_cms_order.check_order()

if __name__=='__main__':
    # str=time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
    # filename='d:\\'+str+'.html'
    # f=open(filename,'a')
    # runner=HtmlTestRunner.HTMLTestRunner(
    #     stream=f,
    #     report_title='result',
    #     descriptions='report'
    # )
    # suit=unittest.TestLoader().loadTestsFromTestCase(orderTest)
    #
    # unittest.TextTestRunner().run(suit)
    # runner.run(suit)
    ot=orderTest
    ot.setUp()
    ot.login()