# -*-conding:utf-8 -*-
# @Time  : 2021/8/29 0029 11:03
# @File  :test_addmember.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
# @describe: 测试添加成员功能

import pytest

from h20_learn.web_auto_test.pages.index_page import IndexPage


class TestAddmember:
    #1、使用setup初始化 indexPage -配合teardown关闭页面 每条用例重新开始
    # 不需要考虑前放用例执行异常，导致页面无法从初始页面开始的问题(设置跳转base_url并不能解决所有异常问题)
    # 但是每条用例都需要重新调用浏览器 比较耗费时间
    #2、使用 setup_class 初始化indexPage -配合teardown_class class执行完毕后关闭
    # 可以节约时间，但是需要考虑用例前后执行异常 带来的影响 可能影响后续用例正常执行
    #todo:用例的数据初始化 -确认账号信息未被注册，如有注册则删除
    #     用例的数据清理 -确认用例执行成功/失败 均需清理添加的成员账号数据

    # def setup_class(self):
    #     self.indexPage = IndexPage()

    def setup(self):
        self.indexPage = IndexPage()
        # self.indexPage.driver.get(self.indexPage.base_url)

    @pytest.mark.parametrize('user,acctid,phone', [('张三1','0011','13101010111'),('张三2','0012','13101010112')])
    def test_index_add_member(self,user,acctid,phone):
        '''
        测试正常添加成员1
        路径：首页 - 添加成员页 - 添加成员
        '''
        phone_list = self.indexPage.goto_add_number().add_member(user,acctid,phone).get_member_list()
        assert phone in phone_list

    @pytest.mark.parametrize('user,acctid,phone',[('李四1','0021','13101010121'),('李四2','0022','13101010122')])
    def test_index_add_member_fail(self,user,acctid,phone):
        '''
        测试 信息重复添加成员失败
        首页 - 添加成员页 - 添加成员 -失败
        '''
        #先增加账号
        phone_list = self.indexPage.goto_add_number().add_member(user,acctid,phone).get_member_list()
        assert phone in phone_list
        #使用相同信息再次注册
        err_messaage_acc,err_messaage_phone = self.indexPage.goto_contact().goto_add_member().add_member_fail(user, acctid, phone)
        assert user in err_messaage_acc
        assert user in err_messaage_phone

    @pytest.mark.parametrize('user,acctid,phone', [('王五1', '0031', '13101010131'),('王五2', '0032', '13101010132')])
    def test_contact_add_member(self,user,acctid,phone):
        '''
        测试正常添加成员2
        路径：首页 - 通讯录页 - 添加成员页 -添加成员
        '''
        phone_list = self.indexPage.goto_contact().goto_add_member().add_member(user,acctid,phone).get_member_list()
        assert phone in phone_list

    def teardown(self):
        self.indexPage.driver.quit()

    # def teardown_class(self):
    #     self.indexPage.driver.quit()

