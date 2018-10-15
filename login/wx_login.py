from login import into_gzh
from tools import vc_tools
import xlrd

class login_class:
    def login_def(self):
        wb=xlrd.open_workbook('D:\\PycharmProjects\\appiumtest\\testdata\\login.xlsx')
        sh=wb.sheet_by_index(0)
        i=0
        phone=''
        while i>=0:
            if sh.cell_value(i,0)=='phone':
                phone=sh.cell_value(i,1)
                break
            i+=1

        wx_login_obj =into_gzh.into_gzh()
        wx_login_obj.setup()
        self.driver=wx_login_obj.driver

        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts.last)
        print(self.driver.current_context)

        # el=self.driver.find_element_by_id('app')
        try:
            el=self.driver.find_element_by_class_name('recommend-box.weui-flex')
            el=self.driver.find_element_by_class_name('recommend-shop_bd')
            el.click()
        except:
            print('没有进入前置页')


        try:
            el=self.driver.find_element_by_class_name('//*[@id="app"]/div[2]/div[2]/div/footer')
            el.click()
        except:
            print('no new gift')


        #clear network data

        el = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/section/div[2]/div/div/div[4]/div[1]')

        el.click()
        vc_tools.driver=self.driver
        vc_tools.clear_network()
        vc_tools.clear_localstorage()



        #wo de
        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/footer/div[2]/a[4]')
        el.click()

        el=self.driver.find_element_by_id('login')
        el.click()

        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[1]/div[1]/div[2]/input')
        el.send_keys(phone)

        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[1]/div[1]/div[3]')
        el.click()

        code=vc_tools.res_network('http://qa.365bencao.cn/malls/api/s_auth_code','code')

        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[1]/div[3]/div[2]/input')
        el.send_keys(code)

        el=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[3]')
        el.click()






if __name__=='__main__':
    wx_login_obj=login_class()
    wx_login_obj.login_def()



