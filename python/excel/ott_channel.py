# coding=utf-8

from matplotlib.pyplot import pink
import xlrd
import pandas as pd


def parse_excle(path: str, sheet: str):
    df = pd.read_excel(path, sheet, keep_default_na=False)
    line = '''
          {}\t{}\t{}\t2023-07-23
          '''
    # print(df.columns.values)
    # print(df.values)
    for idx, row in df.iterrows():
        if idx > 0:
            print(row['UUID'])

        #print(line.format(company, plat, row['page_code'], row['page_name'], row['page_type'], row['start_version'], row['remarks'], row['wiki']))



parse_excle("D:\\新英\\数据需求\\BI指标及维度需求-2022.2.23.xls", "2021年6月同步")
# import_dict_event("C:\\Users\\Hello\\Downloads\\dict_page_420.xls", "all")
