# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://qa.365bencao.cn/malls/sys/login")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("tujinliang")
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys("tujinliang")
        driver.find_element_by_id("loginButton").click()
        driver.find_element_by_link_text(u"商品").click()
        driver.find_element_by_link_text(u"RMB商品").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='RMB源商品'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='未标记'])[1]/following::button[1]").click()
        self.assertEqual(u"零售价必须大于零", self.close_alert_and_get_its_text())
        driver.find_element_by_link_text("15").click()
        driver.find_element_by_name("campuses").click()
        Select(driver.find_element_by_name("campuses")).select_by_visible_text("tjl0408")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='当前校区：'])[1]/following::option[44]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='未标记'])[1]/following::button[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='取消'])[1]/following::button[1]").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("tujinliang")
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys("tujinliang")
        driver.find_element_by_name("userName").click()
        driver.find_element_by_name("userName").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | name=userName | ]]
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys("tjl041602")
        driver.find_element_by_xpath("//body").click()
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | name=password | ]]
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("tjl041602")
        driver.find_element_by_xpath("//body").click()
        driver.find_element_by_id("loginButton").click()
        driver.find_element_by_link_text(u"订单管理").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='进货自储'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='RMB(校内配送)'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='备注'])[2]/following::button[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='快递单号：'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='快递单号：'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='快递单号：'])[1]/following::input[1]").send_keys("123")
        driver.find_element_by_id("addLogis").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='取消'])[1]/following::button[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='修改物流'])[1]/following::button[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='提示'])[1]/following::button[1]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
