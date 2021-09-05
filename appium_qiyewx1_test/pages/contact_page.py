# -*-conding:utf-8 -*-
# @Time  : 2021/9/5 0005 10:32
# @File  :contact_page.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
# @describe: 通讯录页
from appium.webdriver.common.mobileby import MobileBy

from h20_learn.appium_qiyewx1_test.pages.add_member_page import AddMemberPage
from h20_learn.appium_qiyewx1_test.pages.basepage import BasePage


class ContactPage(BasePage):

    def goto_add_member(self):
        """跳转 添加成员页"""
        # self.click(MobileBy.XPATH, "//*[@text='添加成员']")
        # self.swipe_find_uiautomator("添加成员")
        self.swipe_find("添加成员")

        return AddMemberPage(self.driver)




