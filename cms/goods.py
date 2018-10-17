from selenium import  webdriver
from selenium.webdriver.support.select import Select
import unittest,time
from selenium.webdriver.common.keys import Keys
from initial import  selenium_init
class cmsGoods(unittest.TestCase):
    goodsName = 'autoTjl' + time.strftime('%m%d%H%M', time.localtime())
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://qa.365bencao.cn/malls/sys/index#')
        self.driver.implicitly_wait(30)
        el=self.driver.find_element_by_name('userName')
        el.clear()
        el.send_keys('tujinliang')

        el=self.driver.find_element_by_name('password')
        el.clear()
        el.send_keys('tujinliang')

        time.sleep(1)
        el=self.driver.find_element_by_id('loginButton')
        el.click()
        time.sleep(1)

    def tearDown(self):
        s = time.strftime('%m-%d-%H:%M', time.localtime())
        selenium_init.driver.get_screenshot_as_png(s + 'sel.png')
        print('save_screenshot')
        self.driver.quit()
    def testAddGoods(self):
        el=self.driver.find_element_by_xpath('//*[@id="navbar_top"]/li[2]/a')
        assert el.text=='商品'
        el.click()
        # sidebar_menu > li:nth-child(2) > a > span:nth-child(2)
        el=self.driver.find_element_by_xpath('/html/body/div/aside[1]/section/ul/li[2]/a/i')
        el.click()
        el.click()

        el=self.driver.find_element_by_xpath('//*[@id="sidebar_menu"]/li[2]/ul/li[1]/a/span')
        el.click()

        el=self.driver.find_element_by_xpath('//*[contains(@onclick,"goEdit()")]')
        assert el.text=='添加'
        el.click()

        el=self.driver.find_element_by_xpath('//*[@id="classifys"]/button[2]')
        el.click()

        el=self.driver.find_element_by_id('nextStep')
        el.click()

        el=self.driver.find_element_by_name('goodsName')
        el.clear()
        el.send_keys(self.goodsName)

        el=self.driver.find_element_by_name('coverImgDescription')
        el.clear()
        el.send_keys('coverImgDescription')

        time.sleep(1)
        el=self.driver.find_element_by_xpath('//*[@id="page_1"]/div[6]/div/a/input')
        el.send_keys('E:\\tjl个人\\测试过程\\微商城4.0\\cstp\\3.png')

        time.sleep(3)
        el=self.driver.find_element_by_xpath('//*[@id="page_1"]/div[7]/div/a/input')
        el.send_keys('E:\\tjl个人\\测试过程\\微商城4.0\\cstp\\160x160.jpg')

        el=self.driver.find_element_by_name('addSpecBtn')
        el.click()

        el=self.driver.find_elements_by_name('specValue')
        el[0].send_keys('red')
        el[1].send_keys('white')

        el=self.driver.find_element_by_xpath('//*[@id="page_1"]/div[10]/div/a/input')
        el.send_keys('E:\\tjl个人\\测试过程\\微商城4.0\\cstp\\750x286.jpg')

        #切换iframe
        el=self.driver.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe')
        self.driver.switch_to.frame(el)

        el=self.driver.find_element_by_tag_name('body')
        el.send_keys('11111111111')

        self.driver.switch_to.default_content()

        el=self.driver.find_element_by_xpath('//*[@id="page_1"]/div[14]/div/a/input')
        el.send_keys('E:\\tjl个人\\测试过程\\微商城4.0\\cstp\\750x600.jpg')

        time.sleep(3)#wait for upload file
        el=self.driver.find_element_by_id('nextStep')
        el.click()

        time.sleep(1)#wait for page to be refreshed
        el=self.driver.find_element_by_name('goodsName')
        el.clear()
        el.send_keys(self.goodsName)
        el.send_keys(Keys.ENTER)

        el=self.driver.find_element_by_xpath('//*[@id="dataTable"]/tbody/tr/td[10]/button[4]')
        assert el.text=='出售'
        el.click()

        el = self.driver.find_element_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="确定"]')
        el.click()

    def notestUpdateGoods(self):
        el = self.driver.find_element_by_xpath('//*[@id="navbar_top"]/li[2]/a')
        assert el.text == '商品'
        el.click()
        # sidebar_menu > li:nth-child(2) > a > span:nth-child(2)
        el = self.driver.find_element_by_xpath('/html/body/div/aside[1]/section/ul/li[2]/a/i')
        el.click()
        el.click()

        el = self.driver.find_element_by_xpath('//*[@id="sidebar_menu"]/li[2]/ul/li[1]/a/span')
        el.click()

        el=self.driver.find_element_by_name('goodsName')
        el.clear()
        el.send_keys(self.goodsName)
        el.send_keys(Keys.ENTER)

        el=self.driver.find_element_by_xpath('//*[@id="dataTable"]/tbody/tr/td[10]/button[1]')
        el.click()

        # time.sleep(3)#wait for the el to be visible
        # el=self.driver.find_elements_by_xpath('//*[@id="classifys"]/button')
        # el[2].click()
        time.sleep(3)  # wait for upload file
        el = self.driver.find_element_by_id('nextStep')
        el.click()

        #出售
        el=self.driver.find_element_by_xpath('//*[@id="dataTable"]/tbody/tr/td[10]/button[4]')
        el.click()

    def testCheckGoods(self):
        #cms shcoolGoods
        el = self.driver.find_element_by_xpath('//*[@id="navbar_top"]/li[2]/a')
        assert el.text == '商品'
        el.click()
        # sidebar_menu > li:nth-child(2) > a > span:nth-child(2)
        el = self.driver.find_element_by_xpath('/html/body/div/aside[1]/section/ul/li[2]/a/i')
        el.click()
        el.click()

        el=self.driver.find_element_by_xpath('//*[@id="sidebar_menu"]/li[2]/ul/li[2]/a/span')
        el.click()

        el = self.driver.find_element_by_name('goodsName')
        # el.send_keys('autoTjl09281435')
        print(self.goodsName)
        el.send_keys(self.goodsName)

        Select(self.driver.find_element_by_name('campuses')).select_by_visible_text('tjl0408')

        time.sleep(1)
        el=self.driver.find_element_by_xpath('//*[@id="campusGoodsDataTable"]/tbody/tr/td[18]/button[4]')
        el.click()

        el=self.driver.find_element_by_id('td_goodsName')
        # assert el.text==self.goodsName

        el=self.driver.find_element_by_id('moneyPrice')
        el.clear()
        el.send_keys('4.00')

        el = self.driver.find_element_by_id('stockPrice')
        el.clear()
        el.send_keys('2.00')

        el = self.driver.find_element_by_id('costPrice')
        el.clear()
        el.send_keys('1.00')

        el=self.driver.find_element_by_xpath('//*[@id="editPriceForm"]/div[2]/button[2]')
        el.click()

        time.sleep(3)
        self.driver.switch_to.alert.accept()

        time.sleep(1)
        els=self.driver.find_elements_by_xpath('//*[@id="campusGoodsDataTable"]/tbody/tr/td[18]/button')
        assert els[0].text=='零售上架'
        els[0].click()
        # el=self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        # el.click()
        time.sleep(1)
        el=self.driver.find_element_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="确定"]')
        el.click()

        time.sleep(10)
        els = self.driver.find_elements_by_xpath('//*[@id="campusGoodsDataTable"]/tbody/tr/td[18]/button')
        assert els[1].text == '进货上架'
        els[1].click()

        time.sleep(1)
        el = self.driver.find_element_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="确定"]')
        el.click()

        #wms goods
        selenium_init.wms()
        driver=selenium_init.driver
        el=driver.find_element_by_xpath('.//*[normalize-space(text()) and normalize-space(.)="分仓库存"]')
        assert el.text=='分仓库存'
        el.click()

        el=driver.find_element_by_xpath('//*[@id="sidebar_menu"]/li[2]/a/span')
        el.click()

        try:
            driver.switch_to_alert().accept()
        except:
            print("no alert")
        el=driver.find_element_by_name('goodsName')
        el.clear()
        el.send_keys(self.goodsName)
        el.send_keys(Keys.ENTER)
        time.sleep(1)

        el=driver.find_element_by_xpath('//*[@id="dataTable"]/tbody/tr/td[4]')
        print(el.text)
        assert el.text=='tjl0408'

        el=driver.find_element_by_xpath('//*[@id="dataTable"]/tbody/tr/td[5]')
        assert el.text=='tjl0408'

        el=driver.find_element_by_xpath('//*[@id="dataTable"]/tbody/tr/td[15]/button[1]')
        el.click()

        el=driver.find_element_by_xpath('//*[@id="tBody"]/tr[1]/td[7]/button')
        el.click()

        el=driver.find_element_by_xpath('//*[@id="stockChangeForm"]/div[1]/div/div[2]/span')
        assert el.text=='0'

        time.sleep(1)
        el=driver.find_element_by_name('num')
        el.send_keys(100)

        el=driver.find_element_by_xpath('//*[@id="stockChangeForm"]/div[2]/button[2]')
        el.click()

        time.sleep(1)
        el=driver.find_element_by_xpath('//*[@id="dataTable"]/tbody/tr/td[9]')
        assert el.text=='100'

        driver.quit()
if __name__=='__main__':

    suite = unittest.TestSuite()
    suite.addTest(cmsGoods('testAddGoods'))
    suite.addTest(cmsGoods('testCheckGoods'))
    runner = unittest.TextTestRunner()
    runner.run(suite)