from initial import appium_init
from selenium import webdriver
import xhjx_globalset
import re
import json
from appium.webdriver.common.touch_action import TouchAction


def clear_network():
    driver = appium_init.driver
    el = driver.find_element_by_class_name('vc-switch')
    el.click()

    el = driver.find_element_by_id('__vc_tab_network')
    el.click()

    el = driver.find_element_by_xpath('//*[@id="__vconsole"]/div[3]/div[4]/a[3]')
    el.click()

    el = driver.find_element_by_xpath('//*[@id="__vconsole"]/div[3]/div[4]/a[8]')
    el.click()


def clear_localstorage():
    driver = appium_init.driver
    el = driver.find_element_by_class_name('vc-switch')
    el.click()

    el = driver.find_element_by_id('__vc_tab_storage')
    el.click()

    el = driver.find_element_by_xpath('//*[@id="__vconsole"]/div[3]/div[2]/a[12]')
    el.click()

    el = driver.find_element_by_xpath('//*[@id="__vconsole"]/div[3]/div[4]/a[7]')
    el.click()

    driver.switch_to_alert().accept()
    el = driver.find_element_by_xpath('//*[@id="__vconsole"]/div[3]/div[4]/a[8]')
    el.click()


def res_network(interface, key):
    driver = appium_init.driver
    el = driver.find_element_by_class_name('vc-switch')
    el.click()

    try:
        el = driver.find_element_by_id('__vc_tab_network')
        el.click()
    except:
        print('allready in the network')

    el = driver.find_elements_by_class_name('vc-table-col')
    for el1 in el:
        print(el1.text)
        if re.search(interface, el1.text):
            el1.click()
            el2 = driver.find_element_by_tag_name('pre')
            res = el2.text
            res = json.loads(res)
            print(res)
            # hide
            el = driver.find_element_by_xpath('//*[@id="__vconsole"]/div[3]/div[4]/a[8]')
            el.click()
            return res[key]


def move_vc():
    driver = appium_init.driver
    el = driver.find_element_by_class_name('vc-switch')
    x=el.location['x']

    y = el.location['y']
    print(y)
    # print(el.location.x)
    # params = {'duration': 1.0,
    #           'fromX': el.location['x'],
    #           'fromY': el.location['y'],
    #           'toX': el.location['x'],
    #           'toY': el.location['y'] - 100,
    #           'element': el}
    # driver.execute_script('mobile:dragFromToForDuration',params )
    driver.switch_to.context('NATIVE_APP')

    TouchAction(driver).press(x=x,y=y).move_to(x=x,y=y-200).release().perform()  #只支持原生, no H5

    driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
