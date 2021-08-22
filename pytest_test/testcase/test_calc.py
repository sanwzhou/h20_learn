# -*-conding:utf-8 -*-
# @Time  : 2021/8/22 0022 22:13
# @File  :test_calc.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
'''
测试计算器
'''
import logging

import allure
import pytest

from h20_learn.pytest_test.common.get_data import getData

@allure.feature('计算器测试模块')
class Testcalc:

    @allure.story('测试加法-整数')
    @pytest.mark.run(order=-1)
    @pytest.mark.parametrize('x,y,expected',getData.get_value('add').get('datas'),
                             ids=getData.get_value('add').get('ids'))
    def test_add_int(self,get_app_calc,x,y,expected):
        logging.info(f'测试加法-整数功能 参数：{x,y},预期结果：{expected}')
        allure.attach.file(r'C:\Users\swzhou\Desktop\假装有图片.jpg',name='加法图片',
                           attachment_type=allure.attachment_type.JPG)
        assert get_app_calc.add(x,y) == expected

    @allure.story('测试加法-浮点数')
    @pytest.mark.run(order=0)
    @pytest.mark.parametrize('x,y,expected', getData.get_value('float').get('datas'),
                             ids=getData.get_value('float').get('ids'))
    def test_add_float(self, get_app_calc, x, y, expected):
        logging.info(f'测试加法-浮点数功能 参数：{x, y},预期结果：{expected}')
        allure.attach.file(r'C:\Users\swzhou\Desktop\假装有图片.jpg', name='加法图片',
                           attachment_type=allure.attachment_type.JPG)
        assert get_app_calc.add(x, y) == expected

    @allure.story('测试除法-异常情况')
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('x,y,expected', getData.get_value('div').get('error').get('datas'),
                             ids=getData.get_value('div').get('error').get('ids'))
    def test_dev_error(self, get_app_calc, x, y, expected):
        logging.info(f'测试触发-异常情况 参数：{x, y},预期结果：{expected}')
        allure.attach.file(r'C:\Users\swzhou\Desktop\假装有图片.jpg', name='除法图片',
                           attachment_type=allure.attachment_type.JPG)
        try:
            get_app_calc.div(x,y)
        except eval(expected) as e:
            print(e)
        except:
            raise Exception('错误类型 与预期不相符')
        else:
            raise Exception('未报异常')
