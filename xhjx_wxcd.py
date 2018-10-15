from  appium import webdriver

des={}
des["platformName"]="Android"
des["platformVersion"]="4.4"
des["deviceName"]="7N2XEE1588055873"
des['appPackage']='com.tencent.mm'
des['appActivity']='.ui.LauncherUI'
des['chromeOptions']={'androidProcess': 'com.tencent.mm:tools'}

driver=webdriver.Remote('http://localhost:4723/wd/hub', des)

