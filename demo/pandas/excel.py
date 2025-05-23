# coding=utf-8

from matplotlib.pyplot import pink
import xlrd
import pandas as pd


def read_xlsx1(path):
    wb = xlrd.open_workbook(path)
    # 输出所有工作蒲中的工作表
    sheet_names = wb.sheet_names()
    print("sheet_names: {}".format(sheet_names))

    # 通过sheet索引或者名称获取sheet
    data_sheet = wb.sheet_by_index(0)
    print(data_sheet)

    data_sheet1 = wb.sheets()[0]
    print(data_sheet1)

    # 通过sheet获取行数
    rowNum = wb.sheet_by_index(0).nrows
    print("rowNum: {}".format(rowNum))

    # 通过sheet获取列数
    colNum = wb.sheet_by_index(0).ncols
    print("colNum: {}".format(colNum))
    
    # 获取第一行的内容
    print(data_sheet.row_values(1))
    # 获取第一列的内容
    print(data_sheet.col_values(3))

    # 获取单元格内容
    print(data_sheet.cell(2, 4).value)

    # 获取所有单元格内容
    list = []
    for i in range(rowNum):
        rowlist = []
        for j in range(colNum):
            rowlist.append(data_sheet.cell_value(i, j))
        list.append(rowlist)

    # 输出所有单元格的内容
    for i in range(rowNum):
        for j in range(colNum):
            print(list[i][j], '\t\t', end="")
        print()

    # 获取数据单元格的数据类型
    # python读取excel中单元格的内容返回的有5种类型，即上面例子中的ctype:
    # ctype :  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error

    # data_ctype = data_sheet.cell(1, 3).ctype
    # print(data_ctype)


def import_dict_page(path: str, sheet: str):
    df = pd.read_excel(path, sheet, keep_default_na=False)
    sql = '''
          insert ignore into dict_page(company, plat, page_code, page_name, page_type, start_version, remarks, wiki) 
          values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');
          '''
    # print(df.columns.values)
    # print(df.values)
    for idx, row in df.iterrows():
        company = None
        if str.lower(row['company']) in ['onw', 'two']:
            company = row['company']
        elif row['company'] == '一':
            company = 'one'
        elif row['company'] == '二':
            company = 'two'
        else:
            print('站点字段不合法')
            break

        plat = None
        if str.lower(row['plat']) in ['app', 'pc', 'pcw', 'h5', 'ott', 'pad']:
            plat = str.lower(row['plat'])
        else:
            print('终端字段不合法')
            break

        print(sql.format(company, plat, row['page_code'], row['page_name'], row['page_type'], row['start_version'], row['remarks'], row['wiki']))


def import_dict_event(path: str, sheet: str):
    df = pd.read_excel(path, sheet, keep_default_na=False)
    sql = '''
          insert into dict_event(company, plat, event_code, event_name, event_type, remarks) values('{}', '{}', '{}', '{}', '{}', '{}');
          '''
    # print(df.columns.values)
    # print(df.values)
    for idx, row in df.iterrows():
        print(sql.format(row['company'], row['plat'], row['event_code'], row['event_name'], row['event_type'], row['remarks']))


def parse_excle(path: str, sheet: str):
    file_path = "/tmp/tv_channel.txt"
    fo = open(file_path, 'w', encoding='utf8')

    df = pd.read_excel(path, sheet, keep_default_na=False)
    line = '{}\t{}\t{}\t2023-07-23\n'
    for idx, row in df.iterrows():
        s = line.format(row['UUID'], row['厂商'], row['型号'])
        print(s)
        fo.write(s)

    fo.close


parse_excle("~/data/UUID2023.xlsx", "202106")

import_dict_page("~/data/dict_page_420.xls", "all")
