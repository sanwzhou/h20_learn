# -*-conding:utf-8 -*-
# @Time  : 2021/9/5 0005 10:44
# @File  :test_addmember.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
# @describe: 测试添加成员

import pytest

from h20_learn.appium_qiyewx2_test.pages.app import APP
from h20_learn.appium_qiyewx2_test.utils.handle_yml import handleyml


class TestAddMember:

    def setup_class(self):
        self.app = APP()

    def setup(self):
        self.main = self.app.start().go_to_mainpage()

    @pytest.mark.parametrize('name,phone',
                             handleyml.get_value('add','data'),
                             ids=handleyml.get_value('add','ids'))
    def test_add_by_manual(self, name, phone):
        """测试手动添加成员"""
        self.main.goto_contact().goto_add_member().add_member_by_manual().add_member(name, phone).get_toast()
        self.main.driver.back()  # 返回通讯录页，继续添加账号
