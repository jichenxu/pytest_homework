# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/2 20:39
@Auth ： chenxu
@File ：test_calc.py
"""
import allure
import pytest
import yaml

from python_code.calc import Calculator

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    print(add_datas)

@pytest.fixture(params=add_datas)
def get_datas(request):
    data = request.param
    yield data

@allure.feature("计算器")
class TestCalc:

   #加法用例
   @allure.story("加法模块")
   @pytest.mark.run(order=1)
   def test_add(self,get_datas):
      with allure.step("计算两个数相加"):
         calc = Calculator()
         result = calc.add(get_datas[0],get_datas[1])
         if isinstance(result, float):
            result = round(result, 2)
            # 得到相加结果之后写断言
         assert result == get_datas[2]
         print("测试加法")
   #除法用例
   @allure.story("除法模块")
   @pytest.mark.run(order=4)
   def test_div(self):
      print("测试除法")
   #减法用例
   @allure.story("减法模块")
   @pytest.mark.run(order=2)
   def test_sub(self):
      print("测试减法")
   #乘法用例
   @allure.story("乘法模块")
   @pytest.mark.run(order=3)
   def test_mul(self):
      print("测试乘法")

if __name__ == '__main__':
    pytest.main()