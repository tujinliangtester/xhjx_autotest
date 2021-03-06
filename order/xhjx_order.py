
from initial import appium_init,selenium_init
import unittest,time
from tools import common,vc_tools,otherTool
driver = appium_init.driver
class order(unittest.TestCase):
    driver = appium_init.driver
    num = 2
    goodsName = 'autoTjl09300922'
    def setUp(self):
        print('order setup')
    def tearDown(self):
        print('order tearDown')

    def testOrderGoodsdetail(self):
        driver.get(appium_init.qaurl)
        beforeGoodStock=common.wms_goods_stock(self.goodsName)

        common.into_goods_detail_by_homeserch(self.goodsName)

        time.sleep(1)
        try:
            el = driver.find_element_by_class_name('buy-now')
            el.click()
        except Exception as e:
            print(e)
            exit()
            # vc_tools.move_vc()  #后续有时间了在来处理vctool 的移动

        time.sleep(1)
        el=driver.find_element_by_class_name('add')
        el.click()

        # el = driver.find_element_by_tag_name('input')  #无法输入数值
        # el.clear()
        # el.send_keys(self.num)

        els = driver.find_elements_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="下一步"]')
        els[1].click()

        '''
        el = driver.find_element_by_class_name('weui-cell')
        el.click()

       
        try:
            el = driver.find_element_by_class_name('address-list-item')
            el = driver.find_element_by_class_name('icon')
            el.click()
        except:
            el = driver.find_element_by_class_name('weui-cell__bd')
            el.click()

        # 编辑收货地址
        el = driver.find_element_by_class_name('name')
        el.clear()
        el.send_keys()
        '''
        # 选择校外收货地址
        time.sleep(0.5)
        el=driver.find_element_by_class_name('weui-cell__bd')
        el.click()

        js='.address-list-item'
        el=common.find_element_by_js_querySelector(js,0)
        el.click()

        js='.dialog-last'
        el=common.find_element_by_js_querySelector(js,0)
        el.click()

        time.sleep(0.5)
        # el = driver.find_element_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="提交订单"]')
        el=driver.find_element_by_xpath('//*[@id="app"]/div/div/div/footer/div[2]/button')
        el.click()

        time.sleep(10)#enough time to wait for synchronous stock
        afterGoodStock=common.wms_goods_stock(self.goodsName)
        print(beforeGoodStock)
        print(afterGoodStock)
        assert beforeGoodStock-afterGoodStock==2

        # el = driver.find_element_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="确认支付"]')
        time.sleep(1)
        el=driver.find_element_by_xpath('//*[@id="app"]/div/footer')
        el.click()

        # 微信支付
        common.wx_pay()

        time.sleep(0.5)
        assert afterGoodStock==common.wms_goods_stock(self.goodsName)

        #获得金币提示框
        try :
            el=driver.find_element_by_class_name('weui-dialog__ft') #前端谈窗按钮的通用class
            el.click()
        except:
            print("金币提示框 not found")

        #点击屏幕进入订单详情
        dx = 460 / 1080
        dy = 600 / 1920
        common.click_native(dx=dx, dy=dy)

        js = "return document.querySelector('.order-info p').innerText"
        orderno = driver.execute_script(js)
        print(orderno)
        orderno=orderno[5:]
        print(orderno)

        common.wms_rmb_outschool_delivery(orderno)
        common.wms_rmb_outschool_confirmReceipt(orderno)
        driver.get(appium_init.qaurl)
    def testOrderGoodsdetail2Pay(self):
        driver.get(appium_init.qaurl)
        beforeGoodStock = common.wms_goods_stock(self.goodsName)

        common.into_goods_detail_by_homeserch(self.goodsName)

        time.sleep(1)
        try:
            el = driver.find_element_by_class_name('buy-now')
            el.click()
        except Exception as e:
            print(e)
            exit()
            # vc_tools.move_vc()  #后续有时间了在来处理vctool 的移动

        time.sleep(1)
        el = driver.find_element_by_class_name('add')
        el.click()

        # el = driver.find_element_by_tag_name('input')  #无法输入数值
        # el.clear()
        # el.send_keys(self.num)

        els = driver.find_elements_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="下一步"]')
        els[1].click()

        '''
        el = driver.find_element_by_class_name('weui-cell')
        el.click()


        try:
            el = driver.find_element_by_class_name('address-list-item')
            el = driver.find_element_by_class_name('icon')
            el.click()
        except:
            el = driver.find_element_by_class_name('weui-cell__bd')
            el.click()

        # 编辑收货地址
        el = driver.find_element_by_class_name('name')
        el.clear()
        el.send_keys()
        '''
        # 选择校外收货地址
        time.sleep(0.5)
        el = driver.find_element_by_class_name('weui-cell__bd')
        el.click()

        js = '.address-list-item'
        el = common.find_element_by_js_querySelector(js, 0)
        el.click()

        js = '.dialog-last'
        el = common.find_element_by_js_querySelector(js, 0)
        el.click()

        time.sleep(0.5)
        # el = driver.find_element_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="提交订单"]')
        el = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/footer/div[2]/button')
        el.click()

        time.sleep(10)  # enough time to wait for synchronous stock
        afterGoodStock = common.wms_goods_stock(self.goodsName)
        print(beforeGoodStock)
        print(afterGoodStock)
        assert beforeGoodStock - afterGoodStock == 2

        # el = driver.find_element_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="确认支付"]')
        time.sleep(0.5)
        driver.back()

        js='.list_content'
        el=common.find_element_by_js_querySelector(js,0)
        el.click()

        el=driver.find_element_by_class_name('show-status')
        assert el.text=='等待买家付款'

        el=driver.find_element_by_class_name('btn')
        el.click()

        time.sleep(0.5)
        el = driver.find_element_by_xpath('//*[@id="app"]/div/footer')
        el.click()

        # 微信支付
        common.wx_pay()


        time.sleep(0.5)
        assert afterGoodStock == common.wms_goods_stock(self.goodsName)

        # 获得金币提示框
        try:
            el = driver.find_element_by_class_name('weui-dialog__ft')  # 前端谈窗按钮的通用class
            el.click()
        except:
            print("金币提示框 not found")

        js='.list_content'
        el=common.find_element_by_js_querySelector(js,0)
        el.click()

        time.sleep(0.5)
        el = driver.find_element_by_class_name('show-status')
        assert el.text == '商家发货中'

        js = "return document.querySelector('.order-info p').innerText"
        orderno = driver.execute_script(js)
        print(orderno)
        orderno = orderno[5:]
        print(orderno)

        common.wms_rmb_outschool_delivery(orderno)

        common.swipe_down_fresh()
        time.sleep(0.5)
        el = driver.find_element_by_class_name('show-status')
        assert el.text == '商家已发货'

        common.wms_rmb_outschool_confirmReceipt(orderno)
        common.swipe_down_fresh()
        time.sleep(0.5)
        el = driver.find_element_by_class_name('show-status')
        assert el.text == '交易完成'
        driver.get(appium_init.qaurl)
    def testOrderGoodsdetail2PayAutoReceipt(self):
        driver.get(appium_init.qaurl)
        beforeGoodStock = common.wms_goods_stock(self.goodsName)

        common.into_goods_detail_by_homeserch(self.goodsName)

        time.sleep(1)
        try:
            el = driver.find_element_by_class_name('buy-now')
            el.click()
        except Exception as e:
            print(e)
            exit()
            # vc_tools.move_vc()  #后续有时间了在来处理vctool 的移动

        time.sleep(1)
        el = driver.find_element_by_class_name('add')
        el.click()

        # el = driver.find_element_by_tag_name('input')  #无法输入数值
        # el.clear()
        # el.send_keys(self.num)

        els = driver.find_elements_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="下一步"]')
        els[1].click()

        '''
        el = driver.find_element_by_class_name('weui-cell')
        el.click()


        try:
            el = driver.find_element_by_class_name('address-list-item')
            el = driver.find_element_by_class_name('icon')
            el.click()
        except:
            el = driver.find_element_by_class_name('weui-cell__bd')
            el.click()

        # 编辑收货地址
        el = driver.find_element_by_class_name('name')
        el.clear()
        el.send_keys()
        '''
        # 选择校外收货地址
        time.sleep(0.5)
        el = driver.find_element_by_class_name('weui-cell__bd')
        el.click()

        js = '.address-list-item'
        el = common.find_element_by_js_querySelector(js, 0)
        el.click()

        js = '.dialog-last'
        el = common.find_element_by_js_querySelector(js, 0)
        el.click()

        time.sleep(0.5)
        # el = driver.find_element_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="提交订单"]')
        el = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/footer/div[2]/button')
        el.click()

        time.sleep(10)  # enough time to wait for synchronous stock
        afterGoodStock = common.wms_goods_stock(self.goodsName)
        print(beforeGoodStock)
        print(afterGoodStock)
        assert beforeGoodStock - afterGoodStock == 2

        # el = driver.find_element_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="确认支付"]')
        time.sleep(0.5)
        driver.back()

        js='.list_content'
        el=common.find_element_by_js_querySelector(js,0)
        el.click()

        el=driver.find_element_by_class_name('show-status')
        assert el.text=='等待买家付款'

        el=driver.find_element_by_class_name('btn')
        el.click()

        time.sleep(0.5)
        el = driver.find_element_by_xpath('//*[@id="app"]/div/footer')
        el.click()

        # 微信支付
        common.wx_pay()


        time.sleep(0.5)
        assert afterGoodStock == common.wms_goods_stock(self.goodsName)

        # 获得金币提示框
        try:
            el = driver.find_element_by_class_name('weui-dialog__ft')  # 前端谈窗按钮的通用class
            el.click()
        except:
            print("金币提示框 not found")

        js='.list_content'
        el=common.find_element_by_js_querySelector(js,0)
        el.click()

        time.sleep(0.5)
        el = driver.find_element_by_class_name('show-status')
        assert el.text == '商家发货中'

        js = "return document.querySelector('.order-info p').innerText"
        orderno = driver.execute_script(js)
        print(orderno)
        orderno = orderno[5:]
        print(orderno)

        common.wms_rmb_outschool_delivery(orderno)

        common.swipe_down_fresh()
        time.sleep(0.5)
        el = driver.find_element_by_class_name('show-status')
        assert el.text == '商家已发货'

        conf=common.cms_rmborder_conf()
        print(conf)
        t=conf['outSideOrderAutoReceipt']
        t=otherTool.str2float(t)*3600
        time.sleep(t)
        time.sleep(10)
        common.swipe_down_fresh()
        time.sleep(0.5)
        el = driver.find_element_by_class_name('show-status')
        assert el.text == '交易完成'
        driver.get(appium_init.qaurl)
    def testOrderGoodsdetail2PayCansel(self):
        driver.get(appium_init.qaurl)
        beforeGoodStock = common.wms_goods_stock(self.goodsName)

        common.into_goods_detail_by_homeserch(self.goodsName)

        time.sleep(1)
        try:
            el = driver.find_element_by_class_name('buy-now')
            el.click()
        except Exception as e:
            print(e)
            exit()
            # vc_tools.move_vc()  #后续有时间了在来处理vctool 的移动

        time.sleep(1)
        el = driver.find_element_by_class_name('add')
        el.click()

        # el = driver.find_element_by_tag_name('input')  #无法输入数值
        # el.clear()
        # el.send_keys(self.num)

        els = driver.find_elements_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="下一步"]')
        els[1].click()

        # 选择校外收货地址
        time.sleep(0.5)
        el = driver.find_element_by_class_name('weui-cell__bd')
        el.click()

        js = '.address-list-item'
        el = common.find_element_by_js_querySelector(js, 0)
        el.click()

        js = '.dialog-last'
        el = common.find_element_by_js_querySelector(js, 0)
        el.click()

        time.sleep(0.5)
        # el = driver.find_element_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="提交订单"]')
        el = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/footer/div[2]/button')
        el.click()

        time.sleep(10)  # enough time to wait for synchronous stock
        afterGoodStock = common.wms_goods_stock(self.goodsName)
        print(beforeGoodStock)
        print(afterGoodStock)
        assert beforeGoodStock - afterGoodStock == 2

        # el = driver.find_element_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="确认支付"]')
        time.sleep(0.5)
        driver.back()

        js='.list_content'
        el=common.find_element_by_js_querySelector(js,0)
        el.click()

        el=driver.find_element_by_class_name('show-status')
        assert el.text=='等待买家付款'

        driver.back()
        js='.button-pink'
        el=common.find_element_by_js_querySelector(js,0)
        el.click()

        js='.dialog-last'
        el=common.find_element_by_js_querySelector(js,0)
        el.click()

        #all order list tab
        time.sleep(0.5)
        js='.navbar__item'
        el=common.find_element_by_js_querySelector(js,0)
        el.click()

        js = '.list_content'
        el = common.find_element_by_js_querySelector(js, 0)
        el.click()

        el = driver.find_element_by_class_name('show-status')
        assert el.text == '交易关闭 (买家取消)'
        driver.get(appium_init.qaurl)
    def testOrderGoodsdetail2TimeOutCansel(self):
        driver.get(appium_init.qaurl)
        beforeGoodStock = common.wms_goods_stock(self.goodsName)

        common.into_goods_detail_by_homeserch(self.goodsName)

        time.sleep(1)
        try:
            el = driver.find_element_by_class_name('buy-now')
            el.click()
        except Exception as e:
            print(e)
            exit()
            # vc_tools.move_vc()  #后续有时间了在来处理vctool 的移动

        time.sleep(1)
        el = driver.find_element_by_class_name('add')
        el.click()

        # el = driver.find_element_by_tag_name('input')  #无法输入数值
        # el.clear()
        # el.send_keys(self.num)

        els = driver.find_elements_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="下一步"]')
        els[1].click()

        # 选择校外收货地址
        time.sleep(0.5)
        el = driver.find_element_by_class_name('weui-cell__bd')
        el.click()

        js = '.address-list-item'
        el = common.find_element_by_js_querySelector(js, 0)
        el.click()

        js = '.dialog-last'
        el = common.find_element_by_js_querySelector(js, 0)
        el.click()

        time.sleep(0.5)
        # el = driver.find_element_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="提交订单"]')
        el = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/footer/div[2]/button')
        el.click()

        time.sleep(10)  # enough time to wait for synchronous stock
        afterGoodStock = common.wms_goods_stock(self.goodsName)
        print(beforeGoodStock)
        print(afterGoodStock)
        assert beforeGoodStock - afterGoodStock == 2

        # el = driver.find_element_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="确认支付"]')
        time.sleep(0.5)
        driver.back()

        js='.list_content'
        el=common.find_element_by_js_querySelector(js,0)
        el.click()

        el=driver.find_element_by_class_name('show-status')
        assert el.text=='等待买家付款'

        conf=common.cms_rmborder_conf()
        print(conf)
        outTime=conf['outSideOrderTimeout']
        outTime=otherTool.str2float(outTime)*3600
        time.sleep(outTime)
        time.sleep(10)#waitiing for time task done
        common.swipe_down_fresh()

        el = driver.find_element_by_class_name('show-status')
        assert el.text == '交易关闭 (支付超时)'
        driver.get(appium_init.qaurl)

if __name__=='__main__':
    print(1)