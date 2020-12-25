#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_river.py
# @Time      :2020/12/25 10:46
# @Author    :SHUI
import pytest,allure
import os
import logging#日志记录用户的动作

def test_1(water):
    try:
        assert "成功的返回" in water
        logging.info('成功的测试')
    except:
        assert "成功的返回" not in water
        logging.info('不成功的用例')


if __name__ == '__main__':

    pytest.main(['-s','--alluredir','../temp'])
    os.system('allure generate ../temp -o ../report --clean')

