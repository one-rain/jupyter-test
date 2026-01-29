"""
社交媒体数据处理
"""
from ast import Tuple
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
import os
from openpyxl import load_workbook
import pandas as pd

from tools.http_tool import query_match_info

p = Path(__file__).resolve()
current_dir = p.parents[2]

DOUYIN_FIELD_MAPPING = {
    "season": {"title": "直播类目", "type": str},
    "match_name": {"title": "直播名称", "type": str},
    "match_start_time": {"title": "开播时间", "type": str},
    "match_duration": {"title": "时长（分钟）", "type": int},
    "pay_type": {"title": "付免策略", "type": str},
    "price": {"title": "定价（元）", "type": float},
    "sales_quantity": {"title": "售卖数量", "type": int},
    "ticket_flow": {"title": "门票流水", "type": int},
    "ticket_income": {"title": "门票收入", "type": float},
    "live_mode": {"title": "直播方式", "type": str},
    "exposure_count": {"title": "曝光数据（万）_曝光次数", "type": int},
    "exposure_people": {"title": "曝光数据（万）_曝光人数", "type": int},
    "watch_people": {"title": "观众数据_累计观众数", "type": int},
    "watch_count": {"title": "观众数据_累计观看次数", "type": int},
    "peak_online_people": {"title": "观众数据_在线人数峰值", "type": int},
    "avg_watch_people": {"title": "观众数据_平均在线人数（万）", "type": float},
    "avg_play_time": {"title": "观众数据_人均观看时长（分钟）", "type": float},
    "new_followers": {"title": "互动数据_新增关注数", "type": int},
    "comment_people": {"title": "互动数据_评论人数", "type": int},
    "comment_count": {"title": "互动数据_评论数", "type": int},
    "share_count": {"title": "互动数据_分享数", "type": int},
    "like_count": {"title": "互动数据_点赞数", "type": int},
    "reward_count": {"title": "互动数据_打赏次数", "type": int},
    "gift_total": {"title": "互动数据_礼物总额", "type": float},
    "interaction_count": {"title": "互动数据_互动总数", "type": int},
    "exposure_watch_rate": {"title": "曝光-观看率", "type": float},
    "watch_interaction_rate": {"title": "观看-互动率", "type": float},
    "exposure_ticket_rate": {"title": "曝光-购票率", "type": float},
    "watch_ticket_rate": {"title": "观看-购票率", "type": float},
    "watch_sales_rate": {"title": "观看-成交率", "type": float},
    "watch_product_exposure_rate": {"title": "观看-商品曝光率", "type": float},
    "product_exposure_click_rate": {"title": "商品曝光-点击率", "type": float},
    "product_click_sales_rate": {"title": "商品点击-成交率", "type": float},
    "sales_count": {"title": "成交单数", "type": int},
    "sales_income": {"title": "成交金额+礼物收入", "type": float},
    "note": {"title": "备注", "type": str},
}

# 排除的关键词
EXCLUDED_KEY_WORD = ["日报", "其他", "节目", "抽签仪式"]

@dataclass
class ExcelModel():
    """
    表示excel文件中的一个工作表

    Attributes:
        sheet_index (int): 工作表索引
        sheet_name (str): 工作表名称
        df (pd.DataFrame): 工作表数据
        key (str): 唯一标识
    """
    sheet_index: int
    sheet_name: str
    df: pd.DataFrame
    key: Optional[str] = None


def read_social_midia_excel(file_path: str, header_row: int = 0) -> list[ExcelModel]:
    """
    读取excel文件，通过表头关键字锁定社媒数据sheet，并读取数据。
    该方式会将数字字符串自动转换成小数。并移除整行为空的行

    Args:
        file_path (str): excel文件路径
        header_row (int, optional): 表头所在行号，默认第0行. Defaults to 0.

    Returns:
        list[ExcelModel]: 包含所有匹配sheet的列表，每个元素为一个ExcelModel对象
    """
    xls = pd.ExcelFile(file_path)
    matched_sheets = []
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(
            file_path,
            sheet_name=sheet_name,
            nrows=header_row  # 只读表头，极快
        )

        cols = list(map(str, df.columns))
        # 抖音直播数据规则：B列为 “直播名称”、J列为 “直播方式”，R列为 “互动数据”
        if "抖音" in sheet_name and "直播名称" in cols and "直播方式" in cols and "互动数据" in cols:
            print(f"sheet_name: {sheet_name}, col size: {len(cols)}")
            if len(cols) != 36:
                raise ValueError(f"sheet_name: {sheet_name}, col size: {len(cols)}, 不符合抖音直播数据格式要求，请检查是否缺少或多余列。")
            else:
              full_df = pd.read_excel(
                  xls,
                  sheet_name=sheet_name,
                  header=[0, 1],
                  dtype=str
              ).dropna(how='all').reset_index(drop=True) # 移除整行为空的行

              # 去掉字符串列中的tab符
              str_cols = full_df.select_dtypes(include="string").columns
              full_df[str_cols] = full_df[str_cols].apply(
                  lambda s: s.str.replace("\t", " ", regex=False)
              )

              matched_sheets.append(ExcelModel(
                  sheet_index=100+xls.sheet_names.index(sheet_name), # index同一加上100，便于后续处理id
                  sheet_name=sheet_name,
                  df=full_df,
                  key="douyin"
              ))

        # 微信视频号直播数据规则：B列为 “直播名称”、J列为 “直播方式”，R列为 “互动数据”
        if "视频号" in sheet_name and "直播名称" in cols and "直播方式" in cols and "互动数据" in cols:
            print(f"sheet_name: {sheet_name}, col size: {len(cols)}")
            if len(cols) != 27:
                raise ValueError(f"sheet_name: {sheet_name}, col size: {len(cols)}, 不符合微信视频号直播数据格式要求，请检查是否缺少或多余列。")
            else:
              full_df = pd.read_excel(
                  xls,
                  sheet_name=sheet_name,
                  header=[0, 1],
                  dtype=str
              ).dropna(how='all').reset_index(drop=True) # 移除整行为空的行

              # 去掉字符串列中的tab符
              str_cols = full_df.select_dtypes(include="string").columns
              full_df[str_cols] = full_df[str_cols].apply(
                  lambda s: s.str.replace("\t", " ", regex=False)
              )
              matched_sheets.append(ExcelModel(
                  sheet_index=100+xls.sheet_names.index(sheet_name), # index同一加上100，便于后续处理id
                  sheet_name=sheet_name,
                  df=full_df,
                  key="wechat"
              ))

        # 小红书直播数据规则：B列为 “直播名称”、J列为 “直播方式”，T列为 “互动数据”
        if "小红书" in sheet_name and "直播名称" in cols and "直播方式" in cols and "互动数据" in cols:
            print(f"sheet_name: {sheet_name}, col size: {len(cols)}")
            if len(cols) != 38:
                raise ValueError(f"sheet_name: {sheet_name}, col size: {len(cols)}, 不符合小红书直播数据格式要求，请检查是否缺少或多余列。")
            else:
              full_df = pd.read_excel(
                  xls,
                  sheet_name=sheet_name,
                  header=[0, 1],
                  dtype=str
              ).dropna(how='all').reset_index(drop=True) # 移除整行为空的行

              # 去掉字符串列中的tab符
              str_cols = full_df.select_dtypes(include="string").columns
              full_df[str_cols] = full_df[str_cols].apply(
                  lambda s: s.str.replace("\t", " ", regex=False)
              )
              matched_sheets.append(ExcelModel(
                  sheet_index=100+xls.sheet_names.index(sheet_name), # index同一加上100，便于后续处理id
                  sheet_name=sheet_name,
                  df=full_df,
                  key="xiaohongshu"
              ))

    if not matched_sheets:
        raise ValueError("未找到包含指定表头的sheet")

    return matched_sheets


def read_social_midia_excel_with_openpyxl(file_path: str) -> list[ExcelModel]:
    """
    读取excel文件，通过表头关键字锁定社媒数据sheet，并读取数据。
    该方式会将保留数字原始格式，不进行自动转换（计算公式的除外）。

    Args:
        file_path (str): excel文件路径

    Returns:
        list[ExcelModel]: 包含所有匹配sheet的列表，每个元素为一个ExcelModel对象
    """
    matched_sheets = []
    col_size = 36

    file_path = os.path.expanduser(file_path)
    wb_formula = load_workbook(file_path, data_only=False)
    wb_value   = load_workbook(file_path, data_only=True)

    rows = []
    for sheet_name in wb_formula.sheetnames:
        ws_f = wb_formula[sheet_name]
        # 提取表头文本
        header_text = []
        row_cells = ws_f[1]  # openpyxl行号从1开始，header_rows是0索引
        cols = [cell.value for cell in row_cells]
        # 抖音直播数据规则：B列为 “直播名称”、J列为 “直播方式”，R列为 “互动数据”
        if "抖音" in sheet_name and "直播名称" in cols and "直播方式" in cols and "互动数据" in cols:
            print(f"====sheet_name: {sheet_name}, col size: {len(cols)}")
            if cols[col_size-1] != "备注":
                raise ValueError(f"sheet_name: {sheet_name}, col size: {len(cols)}, 不符合抖音直播数据格式要求，请检查是否缺少或多余列。")
            else:
                ws_v = wb_value[sheet_name]
                # 只取前col_size列数据
                for r_f, r_v in zip(ws_f.iter_rows(max_col=col_size), ws_v.iter_rows(max_col=col_size)):
                    row = []
                    for c_f, c_v in zip(r_f, r_v):
                        if c_f.data_type == "f":
                            row.append(c_v.value)   # 公式 → 结果（数值）
                        else:
                            row.append("" if c_f.value is None else str(c_f.value))

                    # 判断整行是否为空
                    if any(row):
                        rows.append(row)
                        #print(row)


def test_process_data(item: ExcelModel):
    """
    数据处理联系

    Args:
        item (ExcelModel): 包含数据的ExcelModel对象

    Returns:
        print
    """

    print(f"sheet_name: {item.sheet_name}")
    print("\n")
    print("="*50)

    print(item.df.columns)
    print("\n")
    print("="*50)

    for col1, col2 in item.df.columns:
        field = f"{col1}"
        if not col2.startswith("Unnamed"):
            field = f"{field}_{col2}"
        print(field)

    print("\n")
    print("="*50)
    df_audience = item.df["观众数据"]
    print(df_audience.head())

    #print(df.values)

    print("\n\n")


def excel_to_csv():
    """
    将excel中社媒直播数据转换为csv文件
    """
    matched_sheets = read_social_midia_excel("~/Downloads/10000002_20260123145802.xlsx")
    #test_process_data(matched_sheets[0])

    for item in matched_sheets:
        if item.key == "douyin":
            process_douyin_data(item)


def process_douyin_data(item: ExcelModel):
    """
    处理抖音数据，将excel中数据转成hive数仓中的观众数据表
    1. 不要表头
    2. 每列之间用制表符隔开
    3. NaN值或其它特殊符号用空字符串替换
    4. 将处理后的数据写入文本文件

    Args:
        item (ExcelModel): 包含抖音数据的ExcelModel对象
    """
    df = item.df
    # 第一列为合并列时，统一处理成上一行的值
    df.iloc[:, 0] = df.iloc[:, 0].ffill()

    # 第一列中有换行符的，根据换行符分割，并取第一个元素作为第一列值
    df.iloc[:, 0] = df.iloc[:, 0].apply(lambda x: x.split('\n')[0] if isinstance(x, str) else x)

    # 其它 NaN 统一转为空字符串
    #df_audience = item.df.fillna("")

    for col in df.columns:
        l0, l1 = col
        # NaN 值统一转为空字符串
        df[col] = df[col].fillna("")
        # "/" 替换为空字符串
        df[col] = df[col].replace("/", "", regex=False)

        # 数值单位统一，将“万”单位转换成“个”整数
        if "（万）" in l0:
            df[col] = pd.to_numeric(df[col], errors="coerce").mul(10000).round(0).astype("Int64").astype(str).replace("<NA>", "")

    # 过滤第2列或第3列为空的行
    mask = (df.iloc[:, 1] == "") | (df.iloc[:, 2] == "")
    if mask.any():
        print("删除第2列或第3列为空的行：")
        #print(df[mask])
        df = df[~mask]

    # 处理列值为 "/" 的情况
    #obj_cols = df_audience.select_dtypes(include="object").columns
    #df_audience[obj_cols] = df_audience[obj_cols].replace("/", "", regex=False)

    # 新增id字段，并输出到第一列。id生成规则：sheet_index_ + (index + 1000)
    df2 = df.copy()
    # 插入到第0列
    df2.insert(0, "id", f"{item.sheet_index}_" + (df2.index + 1000).astype(str))

    df2.to_csv(
        f"{current_dir}/assets/data/social_midia/{item.key}_{item.sheet_index}.txt",
        sep="\t",
        index=False,
        header=False,
        encoding="utf-8"
    )


def match_match_id():
    """
    匹配赛事id

    Args:
        item (ExcelModel): 包含抖音数据的ExcelModel对象
    """
    data_files = ["douyin_103.txt", "douyin_114.txt", "douyin_115.txt", "douyin_116.txt"]
    # 读取文本文件
    for data_file in data_files:
        df = pd.read_csv(
            f"{current_dir}/assets/data/social_midia/{data_file}",
            sep="\t",
            header=None,
            dtype=str,
            encoding="utf-8"
        )
        print(df.columns)
        print(df.head())
        # 取第一列


if __name__ == '__main__':
    #excel_to_csv()
    print("="*50)
    match_match_id()

