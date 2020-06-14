#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/14 10:48
# @Author  : Chris.Ma
import requests

if __name__ == "__main__":
    r = requests.get("http://www.baidu.com")
    print(r.text)