# -*-conding:utf-8 -*-
# @Time  : 2021/9/12 0012 20:23
# @File  :app.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
# @describe: app相关操作

from appium import webdriver

from h20_learn.appium_qiyewx2_test.pages.basepage import BasePage
from h20_learn.appium_qiyewx2_test.pages.main_page import MainPage


class APP(BasePage):

    def start(self,driver: webdriver = None):
        if driver is None:
            caps = {
                "platformName": "Android",
                "platformVersion": "6.0",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",

                "skipDeviceInitialization": True,
                "skipServerInstallation ": True,
                "noReset": True,
                "dontStopAppOnReset": True,
                "unicodeKeyBoard": True,
                "resetKeyBoard": True
            }
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def go_to_mainpage(self):
        return MainPage(self.driver)

    def stop(self):
        pass

    def restart(self):
        pass

