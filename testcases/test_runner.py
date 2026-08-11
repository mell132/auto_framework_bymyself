import pytest
import requests
from utils.excel_utils import read_excel

class TestRunner:
    #读取测试用例文件中的全部数据，用属性保存
    data=read_excel()

    @pytest.mark.parametrize("case",data)
    def test_case(self,case):
        #解析请求数据

        #发送请求，获得响应结果

        #处理断言

        #提取