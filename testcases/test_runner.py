import pytest
import requests
import jsonpath
from utils.excel_utils import read_excel

class TestRunner:
    #读取测试用例文件中的全部数据，用属性保存
    data=read_excel()
    #提取后的数据需要初始化一个全局的属性来保存，可以使用{}空字典
    all={}

    @pytest.mark.parametrize("case",data)
    def test_case(self,case):
        #解析请求数据
        method = case["method"]
        url = "http://192.168.10.131:8888/api/private/v1"+case["path"]
        headers=eval(case["headers"]) if isinstance(case["headers"],str) else None
        params=eval(case["params"]) if isinstance(case["params"],str) else None
        data=eval(case["data"]) if isinstance(case["data"],str) else None
        json=eval(case["json"]) if isinstance(case["json"],str) else None
        files=eval(case["files"]) if isinstance(case["files"],str) else None

        requests_data={
            "method":method,
            "url":url,
            "headers":headers,
            "params":params,
            "data":data,
            "json":json,
            "files":files,
        }
        #发送请求，获得响应结果
        res=requests.request(**requests_data)
        #处理断言
        if case["check"]:
            assert jsonpath.jsonpath(res.json(),case["check"])[0]==case["expected"]
        else:
            assert case["expected"] in res.text

        #提取