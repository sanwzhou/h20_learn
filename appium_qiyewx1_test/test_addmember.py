# -*-conding:utf-8 -*-
# @Time  : 2021/9/5 0005 10:44
# @File  :test_addmember.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
# @describe: 测试添加成员

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAddMeber:

    @pytest.mark.parametrize('name,phone',
                             [('李四1', '19012330121'), ('李四2', '19012330122'), ('李四3', '19012330123')],
                             ids=['账号李四1', '账号李四2', '账号李四3'])
    def test_add(self,name,phone):
        """非po形式"""
        caps = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",

            "skipDeviceInitialization": True,
            "skipServerInstallation ": True,
            "noReset": True,
            "dontStopAppOnReset": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True
        }

        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        driver.implicitly_wait(5)
        driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()

        driver.find_element(MobileBy.ID, "com.tencent.wework:id/bf6").send_keys(name)
        driver.find_element(MobileBy.ID, 'com.tencent.wework:id/ge0').send_keys(phone)
        # 取消自动发送邀请
        driver.find_element(MobileBy.XPATH, '//*[@text="保存后自动发送邀请通知"]').click()
        driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        # print(driver.page_source)
        #toast定位 class
        # toast = (MobileBy.XPATH,'//*[class="android.widget.Toast"]')
        #toast定位 包含关键字
        toast = (MobileBy.XPATH,'//*[contains(@text,"添加成功")]')
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(toast))
        # WebDriverWait(driver, 10).until(lambda x: "添加成功" in x.page_source)
        driver.back()  # 返回通讯录页
