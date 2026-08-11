import logging

import allure
import pymysql
import requests

from config.config import *


@allure.step("2.发送http请求")
def send_http_request(**requests_data):
    res = requests.request(**requests_data)
    logging.info(f"2.发送http请求，响应：{res.text}")
    return res

def send_jdbc_request(sql,index=0):
    conn = pymysql.Connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        charset="utf8"
    )
    cur = conn.cursor()
    # 执行语句
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[0]