import allure
import jsonpath

from utils.send_request import send_jdbc_request


def json_extractor(case,all,res):
    if case["jsonExData"]:
        with allure.step("4.json提取"):
            for key, value in eval(case["jsonExData"]).items():
                value = jsonpath.jsonpath(res.json(), value)[0]
                all[key] = value
                # print(all)
def jdbc_extractor(case,all):
    if case["sqlExData"]:
        with allure.step("4.jdbc提取"):
            for key, value in eval(case["sqlExData"]).items():
                value = send_jdbc_request(value)
                all[key] = value
                # print(all)