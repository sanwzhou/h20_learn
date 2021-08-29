# -*-conding:utf-8 -*-
# @Time  : 2021/8/29 0029 15:59
# @File  :save_cookies.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
# @describe: 保存登录cookies

import json
from time import sleep

from selenium import webdriver

from h20_learn.web_auto_test.config.get_config import dir_path


class SaveCookies:

    def save_cookies(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        sleep(20)
        cookies = self.driver.get_cookies()
        print(cookies)

        cookies_file = dir_path / 'config' / 'cookies.json'
        with open(cookies_file,'w') as f:
            json.dump(cookies,f)

        self.driver.quit()

save_cookies = SaveCookies()

if __name__ == '__main__':
    save_cookies.save_cookies()