from selenium import webdriver
import xhjx_cms_order
import xhjx_order_wx_appium17
import time
from selenium.webdriver.support.ui import Select
import xhjx_globalset

wmsgoodsname=''
def login():

    xhjx_cms_order.cmsdriver.get('http://qa.365bencao.cn/warehouse/sys/index')
    el=xhjx_cms_order.cmsdriver.find_element_by_name('userName')
    el.send_keys('tjl3')

    el=xhjx_cms_order.cmsdriver.find_element_by_name('password')
    el.send_keys('123')

    el=xhjx_cms_order.cmsdriver.find_element_by_id('loginButton')
    el.click()

def check_stock():
    try:
        el=xhjx_cms_order.cmsdriver.switch_to.alert
        el.accept()
    except:
        print('no alert found ')
    el=xhjx_cms_order.cmsdriver.find_element_by_xpath('//*[@id="navbar_top"]/li[2]/a')
    el.click()

    #deal the alert
    try:
        el=xhjx_cms_order.cmsdriver.switch_to.alert
        el.accept()
    except:
        print('no alert found ')
    # xhjx_cms_order.cmsdriver.switch_to.alert.accept()

    #goodsname
    time.sleep(2)
    el=xhjx_cms_order.cmsdriver.find_element_by_xpath('//*[@id="goodsListForm"]/div/div[1]/div/input')
    print('wms goodsname:'+wmsgoodsname)
    el.send_keys(wmsgoodsname)

    s1=Select(xhjx_cms_order.cmsdriver.find_element_by_name('state'))
    s1.select_by_index(1)

    #get current stock
    wmsstock=int(xhjx_cms_order.cmsdriver.find_element_by_xpath('//*[@id="dataTable"]/tbody/tr/td[6]').text)
    print('wms stock is ')
    print(wmsstock)
    xhjx_globalset.set_value('stock',str(wmsstock))



    print('wms:111')

#check order
def check_order():
    el=cmsdriver.find_element_by_xpath('//*[@id="navbar_top"]/li[7]/a')
    el.click()

