# -*-conding:utf-8 -*-
# @Time  : 2021/8/29 0029 10:51
# @File  :index_page.py.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
# @describe: 登录首页

from selenium.webdriver.common.by import By

from h20_learn.web_auto_test.pages.add_member_page import AddMemberPage
from h20_learn.web_auto_test.pages.basepage import BasePage
from h20_learn.web_auto_test.pages.contact_page import ContactPage


class IndexPage(BasePage):
    base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_contact(self):
        '''跳转通讯录页'''
        self.click(By.CSS_SELECTOR,'#menu_contacts')
        return ContactPage(self.driver)


    def goto_add_number(self):
        '''跳转添加成员页'''
        self.click(By.CSS_SELECTOR,'.ww_indexImg_AddMember')
        return AddMemberPage(self.driver)

