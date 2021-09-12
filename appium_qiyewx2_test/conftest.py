# -*-conding:utf-8 -*-
# @Time  : 2021/8/22 0022 21:32
# @File  :conftest.py
# @Author:swzhou
# @email :zhou_sanwang@163.com
import os
import time

import pytest



from h20_learn.pytest_test.app.app_calc import app_calc


@pytest.fixture(scope='class')
def get_app_calc():
    return app_calc

@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    rootdir = request.config.rootdir
    log_name = os.path.join(rootdir,'logs', f'{now}.logs')

    request.config.pluginmanager.get_plugin("logging-plugin").set_log_path(log_name)
