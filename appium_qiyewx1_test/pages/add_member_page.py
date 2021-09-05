# -*-conding:utf-8 -*-
# @Time  : 2021/9/5 0005 10:34
# @File  :add_member_page.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
# @describe: 添加成员页
from appium.webdriver.common.mobileby import MobileBy

from h20_learn.appium_qiyewx1_test.pages.add_member_by_Manual_page import AddMemberByManualPage
from h20_learn.appium_qiyewx1_test.pages.basepage import BasePage


class AddMemberPage(BasePage):

    def add_member_by_Manual(self):
        """手动输入添加"""
        self.click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return AddMemberByManualPage(self.driver)

    def get_toast(self):
        """获取toast"""
        return self.wait_find(MobileBy.XPATH,'//*[contains(@text,"添加成功")]')
