import traceback
import os,sys
from time import sleep
from appium import webdriver
import xhjx_cms_order
import HtmlTestRunner
import xhjx_wms_order
import xhjx_globalset


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
goodsname=''
stock=0
stock_before=0
stock_after=0
username=''
orderno=''
goods_num=7
shopcar_goodsname=''

# class orderTest(unittest.TestCase):
class orderTest():
    # def setUp(self):
    def setup(self):
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
    def preforweb(self):
        sleep(2)
        el = self.driver.find_element_by_id('com.tencent.mm:id/apy')  # huawei
        # el = self.driver.find_elements_by_id('com.tencent.mm:id/apt')#oppo
        # el1=el[1]
        el.click()

        sleep(2)
        el = self.driver.find_element_by_id('com.tencent.mm:id/adm')
        el.click()

        sleep(5)
        contexts = self.driver.contexts

        for cotext in contexts:
            print(cotext)

        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
        print('current context is: ' + self.driver.context)
        # wo de
        el = self.driver.find_element_by_xpath('//*[@id="app"]/div/footer/div[2]/a[5]')
        el.click()

    def login(self):


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
        el.send_keys(username)

        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[1]/div[1]/div[3]/button')
        el.click()

        #vconsole
        el=self.driver.find_element_by_class_name('vc-switch')
        el.click()

        # el=self.driver.find_element_by_id('__vc_tab_network')
        el=self.driver.find_element_by_xpath('//*[@id="__vc_tab_network"]')
        el.click()

        el=self.driver.find_element_by_xpath('//*[@id="__vc_log_network"]/div/div/div/dl/dd[1]')
        el.click()

        #response
        el=self.driver.find_element_by_xpath('//*[@id="__vc_log_network"]/div/div/div/div/div[2]/div/pre')
        password=el.text[12:18]
        print(password)

        #hide
        el=self.driver.find_element_by_xpath('//*[@id="__vconsole"]/div[3]/div[4]/a[8]')
        el.click()

        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[1]/div[2]/div[2]/input')
        el.send_keys(password)

        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[3]/button')
        el.click()

    def logout(self):
        #我的
        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/footer/div[2]/a[5]')
        el.click()

        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/section/div/aside[2]/i')
        el.click()

        el=self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/a[2]')
        el.click()

        el=self.driver.find_element_by_id('login')
        el.click()

        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[3]')
        el.click()

        #back to wo de
        self.driver.press_keycode(4)


    #用户订单
    def test_user_order_buy(self):
        #go home
        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/footer/div[2]/a[1]')
        el.click()

        #下面的部分已经加入到登陆中
        # sleep(2)
        # el = self.driver.find_element_by_id('com.tencent.mm:id/aoh')#huawei
        # # el = self.driver.find_elements_by_id('com.tencent.mm:id/apt')#oppo
        # # el1=el[1]
        # el.click()
        #
        # sleep(2)
        # el = self.driver.find_element_by_id('com.tencent.mm:id/acs')
        # el.click()
        #
        # sleep(5)
        # contexts = self.driver.contexts
        #
        # for cotext in contexts:
        #     print(cotext)
        #
        #
        # self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
        # print('current context is: '+self.driver.context)

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
        el.send_keys('tjl')#goods  name

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
        try :
            # xhjx_wms_order.login()
            print(1)
        except:
            print('cms or wms login erro')
        sleep(2)
        # xhjx_wms_order.check_stock()


        # stock_before=int(xhjx_globalset.get_value('stock'))

        print('appium stock is ')
        # print(stock_before)

        sleep(2)
        # el=self.driver.find_element_by_class_name('weui-flex-item.buy-now')
        el=self.driver.find_element_by_xpath('//*[@id="goods-detail"]/div[2]/div[3]')
        el.click()

        sleep(2)
        el=self.driver.find_element_by_xpath('//input')
        el.clear()
        el.send_keys(goods_num)


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



        sleep(5)
        el=self.driver.find_element_by_id('com.tencent.mm:id/cke')
        money=el.text
        if money=='¥0.01':

            # el=self.driver.find_element_by_class_name('android.widget.RelativeLayout')
            el=self.driver.find_element_by_id('com.tencent.mm:id/ckg')
            el.send_keys('236323')
        else:
            print('money > 0.01')
            sys.exit()

        # pay finish confirm
        sleep(5)
        el=self.driver.find_element_by_id('com.tencent.mm:id/dri')
        el.click()

        #switch to webview
        sleep(5)
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
        print('current context is :'+self.driver.context)

        #back to goods detail
        self.driver.press_keycode(4)

        #back home
        el=self.driver.find_element_by_xpath('//*[@id="goods-detail"]/div[1]/div/div/div[4]/div')
        el.click()
        #
        #
        # sleep(2)
        # xhjx_wms_order.check_stock()
        # stock_after=int(xhjx_globalset.get_value('stock'))
        #
        # print('before:'+str(stock_before))
        # print('after:'+str(stock_after))
        # stock_reduce=stock_before-stock_after
        # # self.assertEqual(2,self.stock_reduce)
        # if stock_reduce==goods_num:
        #     print('the stock is right')
        # else:
        #     print('the stock is wrong:')
        #     print('reduce is :'+str(stock_reduce)+'    should be :'+str(goods_num))
        #     sys.exit()

    def wd_to_cms(self):
        #我的
        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/footer/div[2]/a[5]')
        el.click()

        #go to cms
        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[2]/div/div')
        el.click()

    def test_user_order_checkoutorder(self):
        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/div[1]/div[2]')
        el.click()

        #待进货
        # el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div[1]')
        # el.click()

        #first one

        el=self.driver.find_element_by_id('app')
        print('app found')

        # el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/div/div[2]/div/div[3]')
        # el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/div/div[2]/div/div[3]/div/div')
        # el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/div/div[2]/div/div[3]/div')
        el=self.driver.find_elements_by_class_name('list_content')
        el1=el[0]
        # el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/div/div[2]/div/div[3]/div/div/div/span[1]')
        # el=self.driver.find_element_by_class_name('weui-flex')
        # el=self.driver.find_element_by_css_selector('#app > div > div > div > div.order-list-content.flex-1 > div:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > span.flex.price')
        # el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/div/div[2]')
        # el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/div/div[2]/div/div[2]/span[2]')
        # el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/div/div[2]/div')
        # el=self.driver.find_element_by_class_name('color-gray')
        el1.click()

        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div[4]/div[1]')
        if orderno==el.text[4:]:
            print('ture:')
            print(orderno)
        else:
            print('out order erro,outorder is:')
            print(el.text[4:])
            print('should be :')
            print(orderno)
    def addshopcar(self):
        # go home
        try :
            el = self.driver.find_element_by_xpath('//*[@id="app"]/div/footer/div[2]/a[1]')
            el.click()
        except:
            print('no need to go home')

        sleep(2)
        el = self.driver.find_element_by_class_name('serBox')
        el.click()

        sleep(2)
        el = self.driver.find_element_by_id('ipt-search')
        el.send_keys(shopcar_goodsname)  # shopcar_goodsname

        sleep(2)
        el = self.driver.find_element_by_id('btn-search')
        el.click()

        sleep(2)
        el = self.driver.find_element_by_class_name('goodsItem')  # first goods
        el.click()

        sleep(2)
        self.goodsname = self.driver.find_element_by_xpath('//*[@id="goods-detail"]/div[1]/div/div/div[3]/h4').text
        print('goodsname:' + self.goodsname)
        xhjx_wms_order.wmsgoodsname = self.goodsname

        # get stock_before
        try :
            xhjx_wms_order.login()
            sleep(2)
        except:
            print('login error or no need to login')
        xhjx_wms_order.check_stock()

        stock_before = int(xhjx_globalset.get_value('stock'))

        print('appium stock is ')
        print(stock_before)

        #add in shopcar
        el=self.driver.find_element_by_xpath('//*[@id="goods-detail"]/div[2]/div[2]')
        el.click()

        el = self.driver.find_element_by_xpath('//*[@id="countControl"]/input')
        # el=self.driver.find_element_by_xpath('//a[@title="我的"]')
        # el=self.driver.find_element_by_tag_name('input')
        el.clear()
        el.send_keys(goods_num)

        el=self.driver.find_element_by_xpath('//*[@id="next"]')
        el.click()

        el=self.driver.find_element_by_xpath('//*[@id="goods-detail"]/div[1]/div/div/div[4]/div/span')
        el.click()

    def shopcar_buy(self):
        #go home
        try :
            el = self.driver.find_element_by_xpath('//*[@id="app"]/div/footer/div[2]/a[1]')
            el.click()
        except:
            print('no need to go home')

        #go to shopcar
        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/footer/div[2]/a[4]')
        el.click()

        #chose all
        el=self.driver.find_element_by_xpath('//*[@id="shoppingCart"]/div[3]/div/p[1]/b')
        el.click()

        el=self.driver.find_element_by_xpath('//*[@id="shoppingCart"]/div[3]/button')
        el.click()

        # wx_pay
        sleep(2)
        el = self.driver.find_element_by_class_name('pay-item')
        el.click()

        # switch for paying
        sleep(1)
        self.driver.switch_to.context('NATIVE_APP')
        print('current context is: ' + self.driver.context)

        sleep(5)
        el = self.driver.find_element_by_id('com.tencent.mm:id/cke')
        money = el.text
        if money == '¥0.01':

            # el=self.driver.find_element_by_class_name('android.widget.RelativeLayout')
            el = self.driver.find_element_by_id('com.tencent.mm:id/ckg')
            el.send_keys('236323')
        else:
            print('money > 0.01')
            sys.exit()

        # pay finish confirm
        sleep(5)
        el = self.driver.find_element_by_id('com.tencent.mm:id/dri')
        el.click()

        # switch to webview
        sleep(5)
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
        print('current context is :' + self.driver.context)

        # back to goods detail
        self.driver.press_keycode(4)

        # back home
        el = self.driver.find_element_by_xpath('//*[@id="goods-detail"]/div[1]/div/div/div[4]/div')
        el.click()

        sleep(2)
        xhjx_wms_order.check_stock()
        stock_after = int(xhjx_globalset.get_value('stock'))

        print('before:' + str(stock_before))
        print('after:' + str(stock_after))
        stock_reduce = stock_before - stock_after
        # # self.assertEqual(2,self.stock_reduce)
        # if stock_reduce == goods_num:
        #     print('the stock is right')
        # else:
        #     print('the stock is wrong:')
        #     print('reduce is :' + str(stock_reduce) + '    should be :' + str(goods_num))
        #     sys.exit()



#全局变量设置


if __name__=='__main__':
    flag=0
    i=0




    #global init
    xhjx_globalset._init()
    #实例化类
    ot=orderTest()

    ot.setup()
    ot.preforweb()

    # #buy user
    username = '12358580002'
    try:
        ot.logout()
    except:
        print('logout erro')
    ot.login()

    while i<10:

        ot.test_user_order_buy()
        i=i+1
        print(i)

    flag=1


