# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/2 21:08
@Auth ： chenxu
@File ：conftest.py.py
"""
import pytest

@pytest.fixture(scope="module",autouse=True)
def print_desc():
   print("开始计算")
   yield
   print("结束计算")