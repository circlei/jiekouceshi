#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_river.py
# @Time      :2020/12/25 10:46
# @Author    :SHUI
import pytest,allure
from common.test_jk import Water_Api
from data.datas import river_case
import os
import logging#日志记录用户的动作
#Water_Api().log_info
'''
class Test_River(object):
    aaa=Water_Api().river
    @allure.story('这是story')
    @allure.title('这title')
    @allure.severity
    @pytest.mark.parametrize("key,river_name",river_case("../data/shujv.yaml"))
    def test_1(self,key,river_name):
        res = self.aaa(key,river_name)
        try:
            assert "成功的返回" in res
            logging.info('有效的输入返回')
        except:
            assert "成功的返回" not in res
            logging.info('无效的输入返回')
'''

def test_1(water):
    try:
        assert "成功的返回" in water
        logging.info('成功的测试')
    except:
        assert "成功的返回" not in water
        logging.info('不成功的用例')


if __name__ == '__main__':
    #pytest.main(['-s'])
    pytest.main(['-s','--alluredir','../temp'])
    os.system('allure generate ../temp -o ../report --clean')

