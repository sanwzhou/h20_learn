# -*-conding:utf-8 -*-
# @Time  : 2021/8/29 0029 21:25
# @File  :add_member_page.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
# @describe: 新增成员页

from time import sleep

from selenium.webdriver.common.by import By

from h20_learn.web_auto_test.pages.basepage import BasePage
from h20_learn.web_auto_test.pages.contact_page import ContactPage


class AddMemberPage(BasePage):

    def add_member(self,user,acctid,phone):
        '''添加成员 输入成员信息'''
        self.send_keys(By.CSS_SELECTOR,'#username',value=user)
        self.send_keys(By.CSS_SELECTOR,'#memberAdd_acctid',value=acctid)
        self.send_keys(By.CSS_SELECTOR,'#memberAdd_phone',value=phone)
        self.click(By.CSS_SELECTOR,'.js_btn_save')
        sleep(1)
        return ContactPage(self.driver)

    def add_member_fail(self, user, acctid, phone):
        '''添加成员失败-输入信息重复'''
        self.send_keys(By.CSS_SELECTOR,'#username',value=user)
        self.send_keys(By.CSS_SELECTOR,'#memberAdd_acctid',value=acctid)
        self.send_keys(By.CSS_SELECTOR,'#memberAdd_phone',value=phone)
        self.click(By.CSS_SELECTOR,'.js_btn_save')
        sleep(1)
        err_messaage_acc = self.find(By.CSS_SELECTOR, '#memberAdd_acctid+div').text
        err_messaage_phone = self.find(By.XPATH, '//*[@id="memberAdd_phone"]/../following-sibling::div[1]').text

        return err_messaage_acc,err_messaage_phone