import openpyxl

from config.config import *

def read_excel(file_path=EXCEL_FILE,sheet_name=SHEET_NAME):
    #打开excel文件
    workbook=openpyxl.load_workbook(file_path)

    #选择表
    worksheet=workbook[sheet_name]
    #读数操作
    data=[]
    keys=[cell.value for cell in worksheet[2]]
    for row in worksheet.iter_rows(min_row=3, values_only=True): #从第三行开始，只返回值
        dict_data=dict(zip(keys, row))
        #如果读取为true，append，否则不append
        if dict_data["is_true"]:
            data.append(dict_data)
    #关闭excel
    workbook.close()
    return data