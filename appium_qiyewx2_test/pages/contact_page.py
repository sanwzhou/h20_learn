# -*-conding:utf-8 -*-
# @Time  : 2021/9/5 0005 10:32
# @File  :contact_page.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
# @describe: 通讯录页

from h20_learn.appium_qiyewx2_test.pages.add_member_page import AddMemberPage
from h20_learn.appium_qiyewx2_test.pages.basepage import BasePage


class ContactPage(BasePage):

    def goto_add_member(self):
        """跳转 添加成员页"""
        self.swipe_find("添加成员")

        return AddMemberPage(self.driver)




