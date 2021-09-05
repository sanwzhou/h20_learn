# -*-conding:utf-8 -*-
# @Time  : 2021/9/5 0005 10:37
# @File  :add_member_by_Manual_page.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
# @describe: 手动输入添加成员页
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from h20_learn.appium_qiyewx1_test.pages.basepage import BasePage


class AddMemberByManualPage(BasePage):

    def add_member(self,name,phone):
        """添加成员"""
        #姓名、手机号
        self.send_keys(MobileBy.ID,"com.tencent.wework:id/bf6",value=name)
        self.send_keys(MobileBy.ID,'com.tencent.wework:id/ge0',value=phone)
        #取消自动发送邀请
        self.click(MobileBy.XPATH,'//*[@text="保存后自动发送邀请通知"]')
        self.click(MobileBy.XPATH,'//*[@text="保存"]')

        from h20_learn.appium_qiyewx1_test.pages.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

