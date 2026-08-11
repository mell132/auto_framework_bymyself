import openpyxl

def read_excel():
    #打开excel文件
    workbook=openpyxl.load_workbook("./data/登录.xlsx")

    #选择表
    worksheet=workbook["Sheet1"]
    #读数操作
    data=[]
    keys=[cell.value for cell in worksheet[2]]
    for row in worksheet.iter_rows(min_row=3, values_only=True): #从第三行开始，只返回值
        dict_data=dict(zip(keys, row))
        data.append(dict_data)
    #关闭excel
    workbook.close()
    return data