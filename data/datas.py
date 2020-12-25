#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :datas.py
# @Time      :2020/12/25 10:42
# @Author    :SHUI
import yaml

def river_case(file):
    with open(f"{file}","r",encoding="utf-8") as f:
        data = yaml.safe_load(f)
        data=data["liuyu"][0]
        #print(data)
    datas = list(zip(data["key"],data["river_name"]))
    return datas


if __name__ == '__main__':
    #river_case("../data/shujv.yaml")
    print(river_case("../data/shujv.yaml"))
