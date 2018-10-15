from selenium import webdriver
import time
import math
import random
driver=webdriver.Firefox()
driver.maximize_window()

def login():
    driver.get('https://dd3-web.jd.com/jdchat/custom.action?jimiFlag=1&entry=jd_fwztc')

if __name__=='__main__':
    login()
    time.sleep(10)

    elt=driver.find_element_by_id('text_in')



    elb=driver.find_element_by_id('sendMsg')
    i=0
    while i<100:
        i+=1
        elt.clear()
        elt.send_keys('有人吗？')
        elb.click()

        print(i)

        sl=random.randint(20,60)
        time.sleep(sl)