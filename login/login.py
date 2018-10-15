import time
from tools import vc_tools
from initial import appium_init
import xlrd

class login_class:
    def setup(self):
        driver=appium_init.driver
        wb=xlrd.open_workbook('D:\\PycharmProjects\\appiumtest\\testdata\\login.xlsx')
        sh=wb.sheet_by_index(0)
        i=0
        phone=''
        while i>=0:
            if sh.cell_value(i,0)=='phone':
                phone=sh.cell_value(i,1)
                break
            i+=1
        try:
            el=driver.find_element_by_class_name('recommend-shop_bd')
            el.click()
        except:
            print('没有进入前置页')


        try:
            el=driver.find_element_by_class_name('new_gift__ft')
            el.click()
        except:
            print('no new gift')

        #wo de
        el=driver.find_element_by_xpath('//*[@id="app"]/div/footer/div[2]/a[4]')
        el.click()

        el=driver.find_element_by_id('login')
        el.click()

        time.sleep(3)
        el=driver.find_elements_by_class_name('weui-input')[0]
        el.send_keys(str(phone))

        el=driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[1]/div[1]/div[3]')
        el.click()


        code=vc_tools.res_network('s_auth_code','code')

        time.sleep(3)
        el = driver.find_elements_by_class_name('weui-input')[2]
        el.click()
        el.send_keys(code)

        el=driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[3]')
        el.click()



if __name__=='__main__':
    wx_login_obj=login_class()
    wx_login_obj.login_def()



