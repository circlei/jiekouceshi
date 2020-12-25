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
        #"Content-Type":"application/x-www-form-encoded"
    }
@pytest.fixture(scope='function',
                params=river_case("../data/shujv.yaml"),
                name="water",
                autouse=True)
def river(request):
    #key="080deff605d2903e60a0bf3eb4b94884"
    #流域名称有http://web.juhe.cn:8080/environment/water/river
    #river=["淮河流域","长江流域","太湖流域","松花江流域","黄河流域","巢湖流域","东南诸河","辽河流域","珠江流域","海河流域","滇池流域","西南诸河"]
    url="http://web.juhe.cn:8080/environment/water/river"

    #参数的写法：get的时候将参数赋值给params
               # post请求的时候将参数赋值给data(注意编码方式,2.添加content-type)
    query=f"key={request.param[0]}&river={request.param[1]}"#.encode()
    res=requests.get(url,headers=head,params=query)
    return res.text

