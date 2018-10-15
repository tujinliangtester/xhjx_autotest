from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

cmsdriver=webdriver.Firefox()
cmsdriver.maximize_window()


def login():
    #login
    cmsdriver.get('http://qa.365bencao.cn/malls/sys/login')
    el=cmsdriver.find_element_by_name('userName')
    el.send_keys('tujinliang')

    el=cmsdriver.find_element_by_name('password')
    el.send_keys('tujinliang')

    el=cmsdriver.find_element_by_id('loginButton')
    el.click()
#check stock
def check_stock():

    print('cms:111')

#check order
def check_order():
    el=cmsdriver.find_element_by_xpath('//*[@id="navbar_top"]/li[7]/a')
    el.click()

#just for temp thing
if __name__=='__main__':
    login()
    time.sleep(1)
    el=cmsdriver.find_element_by_xpath('/html/body/div/header/nav/div/ul/li[2]')
    el.click()

    el=cmsdriver.find_element_by_xpath('//*[@id="sidebar_menu"]/li[4]/a/span[1]')
    el.click()

    el=cmsdriver.find_element_by_xpath('//*[@id="sidebar_menu"]/li[4]/ul/li[2]/a/span')
    el.click()

    # el=cmsdriver.find_element_by_name('campuses')
    s=Select(cmsdriver.find_element_by_name('campuses'))
    time.sleep(1)
    s.select_by_value('81')


    i=0
    while(i<11):
        i = i + 1
        j=i
        el = cmsdriver.find_element_by_name('goodsName')
        if j<10:
            j='0'+str(j)
        gn='tjl0411'+j
        el.clear()
        el.send_keys(gn)

        # el = cmsdriver.find_element_by_xpath('//*[@id="campusGoodsQueryForm"]/div/div[1]/div/div/button')
        # el.click()


        try:
            el=cmsdriver.find_element_by_xpath('//*[@id="campusGoodsDataTable"]/tbody/tr[1]/td[14]/button[3]')
            el.click()
        except:
            el=cmsdriver.find_element_by_xpath('//*[@id="campusGoodsDataTable"]/tbody/tr[1]/td[14]/button[1]')
            el.click()
            el=cmsdriver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
            el.click()

            time.sleep(1)
            el = cmsdriver.find_element_by_xpath('//*[@id="campusGoodsDataTable"]/tbody/tr[1]/td[14]/button[3]')
            el.click()

        el=cmsdriver.find_element_by_id('moneyPrice')
        el.clear()
        el.send_keys('3.33')

        el=cmsdriver.find_element_by_id('stockPrice')
        el.clear()
        el.send_keys('2.22')

        el=cmsdriver.find_element_by_id('costPrice')
        el.clear()
        el.send_keys('1.11')

        el=cmsdriver.find_element_by_xpath('//*[@id="editPriceForm"]/div[2]/button[2]')
        el.click()

        time.sleep(1)
        cmsdriver.switch_to_alert().accept()

        time.sleep(1)
        el=cmsdriver.find_element_by_xpath('//*[@id="campusGoodsDataTable"]/tbody/tr[1]/td[14]/button[1]')
        el.click()

        el=cmsdriver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
        el.click()
