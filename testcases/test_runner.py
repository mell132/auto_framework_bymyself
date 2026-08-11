import logging

import pytest
from jinja2 import Template


from utils import analyse_case, send_request
from utils.allure_utils import allure_init
from utils.asserts import http_assert, jdbc_assert
from utils.excel_utils import read_excel
from utils.analyse_case import analyse_case
from utils.extractor import json_extractor, jdbc_extractor
from utils.send_request import send_http_request, send_jdbc_request


class TestRunner:
    #读取测试用例文件中的全部数据，用属性保存
    data=read_excel()
    #提取后的数据需要初始化一个全局的属性来保存，可以使用{}空字典
    all={}

    @pytest.mark.parametrize("case",data)
    def test_case(self,case):
        all=self.all
        #引用全局变量，根据all的值渲染case
        case=eval(Template(str(case)).render(all))

        #初始化allure报告
        allure_init(case)

        #测试用例的描述信息
        logging.info(f"用例ID:{case["id"]} 模块：{case["feature"]} 场景：{case["story"]} 标题：{case["title"]}")
        #解析请求数据
        requests_data=analyse_case(case)
        #发送请求，获得响应结果
        res= send_http_request(**requests_data)
        #处理断言
        #http断言
        http_assert(case, res)

        #数据库断言
        jdbc_assert(case)
        #提取
        #json提取
        json_extractor(case,all,res)

        #数据库提取
        jdbc_extractor(case,all)
