
from initial import appium_init
import unittest,time
from tools import common,vc_tools
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
        time.sleep(1)
        # el = driver.find_element_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="提交订单"]')
        el=driver.find_element_by_xpath('//*[@id="app"]/div/div/div/footer/div[2]/button')
        el.click()

        time.sleep(0.5)
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

        el0=driver.find_element_by_class_name('order-info')
        el=el0.find_element_by_xpath('.//p[0]')
        print('............................')
        print(el.text)

        common.wms_rmb_outschool_delivery()

goodsName=''
def commit_order_goodsdetail(num):
    common.into_goods_detail_by_homeserch(goodsName)
    el=driver.find_element_by_class_name('buy-now')
    el.click()

    el=driver.find_element_by_tag_name('input')
    el.clear()
    el.send_keys(num)

    el=driver.find_element_by_id('next')
    el.click()

    el=driver.find_element_by_class_name('weui-cell')
    el.click()

    try:
        el=driver.find_element_by_class_name('address-list-item')
        el=driver.find_element_by_class_name('icon')
        el.click()
    except:
        el=driver.find_element_by_class_name('weui-cell__bd')
        el.click()

    #编辑收货地址
    el=driver.find_element_by_class_name('name')
    el.clear()
    el.send_keys()

if __name__=='__main__':
    commit_order_goodsdetail(1)