# -*-conding:utf-8 -*-
# @Time  : 2021/9/5 0005 9:51
# @File  :basepage.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
# @describe: 基类
import logging

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: webdriver = None):
        self.driver = driver

    def log_info(self,message):
        logging.info(message)

    def find(self, by, locator=None):
        self.log_info(f'查找元素：({by},{locator})')
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    def finds(self, by, locator=None):
        self.log_info(f'查找多个元素：({by},{locator})')
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_elements(*by)

    def click(self, by, locator=None):
        self.log_info(f'点击元素：({by},{locator})')
        self.find(by, locator).click()

    def send_keys(self, by, locator=None, *, value):
        self.log_info(f'输入内容：({by},{locator})')
        self.find(by, locator).clear()
        self.find(by, locator).send_keys(value)

    def wait_find(self, by, locator=None):
        ele = (by, locator)
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(ele))

    def swipe_find_uiautomator(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector().scrollable(true).\
                                 instance(0)).scrollIntoView(new UiSelector().\
                                 text({text}).instance(0));').click()

    def swipe_find(self, text, num=3):
        """滑动查找"""
        size = self.driver.get_window_size()
        width = size.get('width')
        height = size.get('height')
        start_x = end_x = width / 2
        start_y = height * 0.8
        end_y = height * 0.2
        duration = 2000
        for i in range(num):
            try:
                ele = self.click(MobileBy.XPATH, f'//*[@text="{text}"]')
                return ele
            except:
                self.driver.swipe(start_x,start_y, end_x, end_y, duration)
        else:
            raise NoSuchElementException('未找到元素')

    def teardown(self):
        self.driver.quit()
