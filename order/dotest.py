from initial import appium_init
from tools import vc_tools,common
from login import login
from appium.webdriver.common.touch_action import TouchAction
import time

if __name__=='__main__':
    driver=appium_init.driver
    print(driver.contexts)
    driver.get('http://qaservice.365bencao.cn/home')

    # el=driver.find_element_by_accessibility_id('vConsole')
    # el.click()


    print('manually move the vconsole in 10s')
    time.sleep(10)

    driver.switch_to.context('CHROMIUM')
    vc_tools.clear_localstorage()
    vc_tools.clear_network()

    login_obj=login.login_class()
    login_obj.setup()

    #wdnm暂未抽离数据
    common.chang_wd('3016')

    common.into_goods_detail_by_homeserch('tjl')




