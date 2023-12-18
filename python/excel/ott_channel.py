# coding=utf-8

import pandas as pd


def parse_excle(path: str, sheet: str):
    file_path = "/tmp/iqiyi_tv_channel.txt"
    fo = open(file_path, 'w', encoding='utf8')

    df = pd.read_excel(path, sheet, keep_default_na=False)
    line = '{}\t{}\t{}\t2023-07-23\n'
    for idx, row in df.iterrows():
        s = line.format(row['UUID'], row['厂商'], row['型号'])
        print(s)
        fo.write(s)

    fo.close


parse_excle("/mnt/d/新英/数据需求/奇异果渠道UUID2023.xlsx", "202106")
