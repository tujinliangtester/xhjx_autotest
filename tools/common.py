from initial import appium_init,selenium_init
from selenium.webdriver.common.keys import Keys
driver = appium_init.driver
cms_driver=selenium_init.driver
import time


def chang_wd(wdnm):
    driver.get('http://qaservice.365bencao.cn/lead?valid=true')

    el = driver.find_element_by_class_name('search-shop')
    el.click()

    el = driver.find_element_by_id('ipt-search')
    el.send_keys(wdnm)

    el = driver.find_element_by_id('btn-search')
    el.click()

    try:
        el = driver.find_element_by_class_name('result_item')
        el.click()
    except:
        print('no wd found')


def home_serch_goods(goods):
    el = driver.find_element_by_class_name('serBox ')
    el.click()

    el = driver.find_element_by_id('ipt-search')
    el.send_keys(goods)

    el = driver.find_element_by_id('btn-search')
    el.click()


def into_goods_detail_by_homeserch(goods):
    time.sleep(1)
    #循环查找元素。。。
    i = 0
    while i < 3:
        i += 1
        print(i)
        try:
            # el = driver.find_element_by_class_name('serBox ')
            el = driver.find_element_by_xpath('//*[@id="app"]/div/header/div/div/div[2]/i')
            el.click()
            break
        except Exception as e:
            print(e)
        try:
            el = driver.find_element_by_class_name('serBox ')
            # el=driver.find_element_by_xpath('//*[@id="app"]/div/header/div/div/div[2]/i')
            el.click()
            break
        except Exception as e:
            print(e)
        try:
            el =driver.find_element_by_tag_name('i')
            el.click()
            break
        except Exception as e:
            print(e)

    time.sleep(1)
    el = driver.find_element_by_id('ipt-search')
    el.send_keys(goods)

    el = driver.find_element_by_id('btn-search')
    el.click()

    # first goods
    time.sleep(1)
    el = driver.find_element_by_xpath('//*[@id="goodspullrefresh"]/div[2]/div/div/div[2]/div')
    el.click()



def address_in(name, phone, campus, dormitory, address, mr, btn):
    el = driver.find_element_by_name('name')
    el.clear()
    el.send_keys(name)

    el = driver.find_element_by_name('phone')
    el.clear()
    el.send_keys(phone)

    el = driver.find_element_by_name('campus')
    el.clear()
    el.send_keys(campus)

    el = driver.find_element_by_name('dormitory')
    el.clear()
    el.send_keys(dormitory)
def wx_pay():
    # 微信支付
    driver.switch_to.context('NATIVE_APP')
    print('switch to native')
    print(driver.current_context)
    el = driver.find_element_by_id('com.tencent.mm:id/d7g')
    assert el.text == '¥0.01'

    el = driver.find_element_by_id('com.tencent.mm:id/c7u')
    el.send_keys('236323')

    time.sleep(3)
    el=driver.find_element_by_id('com.tencent.mm:id/ejv')
    el.click()

    driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
    print('switch to web')
    print(driver.current_context)
def wms_goods_stock(goodsName):
    selenium_init.wms()
    el=cms_driver.find_element_by_xpath('//*[@id="navbar_top"]/li[2]')
    el.click()

    el=cms_driver.find_element_by_xpath('//*[@id="sidebar_menu"]/li[2]/a/span')
    el.click()

    el=cms_driver.find_element_by_name('goodsName')
    el.clear()
    el.send_keys(goodsName)
    el.send_keys(Keys.ENTER)

    time.sleep(0.5)
    el=cms_driver.find_element_by_xpath('//*[@id="dataTable"]/tbody/tr/td[9]')
    return int(el.text)
def wms_rmb_outschool_delivery(orderNo):
    selenium_init.wms()
    el=cms_driver.find_element_by_xpath('//*[@id="navbar_top"]/li[4]/a')
    el.click()

    el=cms_driver.find_element_by_xpath('//*[@id="sidebar_menu"]/li[3]/a/span[1]')
    el.click()

    el=cms_driver.find_element_by_xpath('//*[@id="sidebar_menu"]/li[3]/ul/li[2]/a/span')
    el.click()

    el=cms_driver.find_element_by_name('combinOrderNo')
    el.clear()
    el.send_keys(orderNo)
    el.send_keys(Keys.ENTER)

    el=cms_driver.find_element_by_xpath('//*[@id="rmbOrderOutsideBaseInfoDataTable"]/tbody/tr/td[19]/button[2]')
    el.click()

    el=cms_driver.find_element_by_name('logisNo')
    el.clear()
    el.send_keys('auto'+orderNo)

    el=cms_driver.find_element_by_id('addLogis')
    el.click()

    el = cms_driver.find_element_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="确定"]')
    el.click()
