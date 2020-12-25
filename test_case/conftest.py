#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :conftest.py
# @Time      :2020/12/25 14:05
# @Author    :SHUI
#
import pytest
import requests
from data.datas import river_case

head = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    }
@pytest.fixture(scope='function',
                params=river_case("E:/ff/data/shujv.yaml"),
                name="water",
                autouse=True)
def river(request):
   
    url="http://web.juhe.cn:8080/environment/water/river"
    query=f"key={request.param[0]}&river={request.param[1]}"
    res=requests.get(url,headers=head,params=query)
    return res.text

