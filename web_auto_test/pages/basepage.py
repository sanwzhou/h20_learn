# -*-conding:utf-8 -*-
# @Time  : 2021/8/29 0029 10:26
# @File  :basepage.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
# @describe: 基础basepage

import json
from time import sleep

from selenium import webdriver

from h20_learn.web_auto_test.config.get_config import dir_path


class BasePage:
    base_url = ''

    def __init__(self,driver: webdriver = None):
        '''判断初始化driver'''
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self.driver.get(self.base_url)

            with open(dir_path / 'config' / 'cookies.json') as f:
                cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            sleep(1)
        else:
            self.driver = driver

        if self.base_url != '':
            self.driver.get(self.base_url)

    def find(self,by,locator=None):
        if locator is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by,value=locator)

    def finds(self,by,locator=None):
        if locator is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by=by,value=locator)

    def click(self,by,locator=None):
        self.find(by,locator).click()

    def send_keys(self,by,locator=None,*,value):
        self.find(by,locator).clear()
        self.find(by,locator).send_keys(value)


