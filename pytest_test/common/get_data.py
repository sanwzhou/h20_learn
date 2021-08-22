# -*-conding:utf-8 -*-
# @Time  : 2021/8/22 0022 21:49
# @File  :get_data.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
'''
获取配置
'''


from pathlib import Path

import yaml

project_path = Path().cwd().parent

class GetData:

    def load_yaml(self,file = None):
        if file == None:
            file = project_path / 'data' /'data.yaml'
        with open(file,encoding='utf8') as f:
            return yaml.safe_load(f)

    def get_value(self,key =None):
        data = self.load_yaml().get('data')
        return data.get(key) if key else data

getData = GetData()

if __name__ == '__main__':
    print(getData.get_value())
    print(getData.get_value('add'))