# -*-conding:utf-8 -*-
# @Time  : 2021/9/5 0005 10:29
# @File  :main_page.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
# @describe: 主页 -消息页
from appium.webdriver.common.mobileby import MobileBy

from h20_learn.appium_qiyewx1_test.pages.basepage import BasePage
from h20_learn.appium_qiyewx1_test.pages.contact_page import ContactPage


class MainPage(BasePage):

    def goto_contact(self):
        """跳转通讯录页"""
        self.click(MobileBy.XPATH,"//*[@text='通讯录']")

        return ContactPage(self.driver)