from initial import appium_init

import xlrd
import time

class into_gzh:
    driver=''
    def setup(self):
        ai = appium_init.appium_ini()
        ai.setup()
        ai.driver.implicitly_wait(20)
        self.driver=ai.driver

        #read data for gzh
        wb=xlrd.open_workbook('D:\\PycharmProjects\\appiumtest\\testdata\\gzh.xlsx')
        sh=wb.sheet_by_index(0)
        i=1
        while i>0:
            print(i)
            print(sh.cell_value(i,0))
            if sh.cell_value(i,0)=='begin':
                while sh.cell_value(i+1,0)!='end':
                    id=sh.cell_value(i+1,1)
                    print(id)
                    if id=='com.tencent.mm:id/aaq':#middle buttone
                        el = ai.driver.find_elements_by_id(id)[1]
                    else:
                        el = ai.driver.find_element_by_id(id)
                    el.click()

                    time.sleep(5)
                    i+=1
            elif sh.cell_value(i,0)=='end':
                break
            i+=1


if __name__=='__main__':
    wx_login_obj=into_gzh()
    wx_login_obj.setup()



