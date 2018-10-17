from appium import webdriver
import xhjx_globalset
import xlrd
import time
from appium.webdriver.common.touch_action import TouchAction

qaurl='http://qaservice.xuehuistore.cn'
wb=xlrd.open_workbook('..\\testdata\\init.xlsx')
sh=wb.sheet_by_name('appium')
desired_caps = {}
i=0
flag='begin'
while i<100:
    i+=1
    print(sh.cell_value(i,0))

    if sh.cell_value(i, 0) == 'begin':
        while sh.cell(rowx=i+1, colx=0):
            i+=1
            if sh.cell_value(i,0)=='end':
                break
            if sh.cell(rowx=i, colx=1):
                print(i)
                key=sh.cell_value(rowx=i, colx=0)
                val=sh.cell_value(rowx=i, colx=1)
                desired_caps[key]=val

        break

desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}
desired_caps['noReset'] = 'true'
print(desired_caps)
driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(30)

def click_native(dx,dy):
    time.sleep(30)
    driver.switch_to.context('NATIVE_APP')
    print('switch to native')
    print(driver.current_context)
    x = driver.get_window_size()['width'] * dx
    y = driver.get_window_size()['height'] * dy

    actions = TouchAction(driver)
    actions.tap(x=x, y=y)
    actions.perform()

    time.sleep(3)

if(desired_caps['deviceName']=='7N2XEE1588055873'):
    # into gzh
    dx=320/720
    dy=200/1280
    click_native(dx,dy)

    dx=410/720
    dy=1230/1280
    click_native(dx,dy)

    time.sleep(3)
    print(driver.contexts)
    # time.sleep(20)
    # driver.get('http://qaservice.365bencao.cn/home')

    driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
    print(driver.current_context)
else:
    # into gzh
    time.sleep(1)
    print('finding azl ')
    el = driver.find_elements_by_id('com.tencent.mm:id/azl')
    el[0].click()

    el = driver.find_elements_by_id('com.tencent.mm:id/aiu')
    el[1].click()

    time.sleep(3)
    print(driver.contexts)

    driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
    print(driver.current_context)



if __name__=='__main__':
    ai=appium_ini()
    ai.setup()

    print(ai.driver.contexts)

    ai.driver.switch_to.context('CHROMIUM')
    ai.driver.get('http://qaservice.365bencao.cn/home')
    time.sleep(5)
    el=ai.driver.find_element_by_id("index-kw")
    el.send_keys('haha')
