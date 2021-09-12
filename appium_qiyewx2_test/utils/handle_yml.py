# -*-conding:utf-8 -*-
# @Time  : 2021/9/12 0012 20:44
# @File  :handle_yml.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
# @describe: 操作yaml文件
import yaml

from h20_learn.appium_qiyewx2_test.utils.get_config import PROGECT_PATH


class HandleYml:

    @staticmethod
    def load(file=None):
        if file is None:
            file = PROGECT_PATH / 'data' / 'member.yml'
        with open(file,encoding='utf8') as f:
            return yaml.safe_load(f)

    def get_value(self,key,value=None,file=None):
        data = self.load(file).get(key)
        return data.get(value) if value else data


handleyml = HandleYml()


if __name__ == '__main__':
    print(handleyml.get_value('add','data'))






