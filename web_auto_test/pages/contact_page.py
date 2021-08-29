# -*-conding:utf-8 -*-
# @Time  : 2021/8/29 0029 10:58
# @File  :contact_page.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
# @describe: 通讯录页面
from time import sleep

from selenium.webdriver.common.by import By


from h20_learn.web_auto_test.pages.basepage import BasePage


class ContactPage(BasePage):

    def goto_add_member(self):
        '''添加成员页'''
        from h20_learn.web_auto_test.pages.add_member_page import AddMemberPage
        sleep(1)
        self.click(By.CSS_SELECTOR,'.js_has_member>div:nth-child(1) a.js_add_member')

        return AddMemberPage(self.driver)


    def get_member_list(self):
        '''获取成员列表'''
        eles = self.finds(By.CSS_SELECTOR,'.member_colRight_memberTable_tr td:nth-child(5)')
        return (ele.text for ele in eles)

    def del_member(self):
        '''删除成员'''
        return self