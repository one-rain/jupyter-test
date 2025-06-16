from operator import indexOf
from os import replace
import pymysql


def db_type_to_str(type: str) -> str:
    ''''
        数据库类型转换汉字
    '''
    if type.find('char') >=0:
        return '字符串'
    elif type.find('int') >=0:
        return '整数'
    elif type.find('double') >=0:
        return '小数'
    elif type.find('float') >=0:
        return '小数'
    elif type.find('date') >=0:
        return '日期'
    elif type.find('time') >=0:
        return '时间'
    else:
        return '字符串'
    


database='test'

conn = pymysql.connect(host='localhost', user='root', password='MswG@2024', database='test', port=3306)
cursor = conn.cursor()
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]
    # 获取表注释
    cursor.execute(f"""
        SELECT TABLE_COMMENT
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s
    """, (database, table))
    table_comment = cursor.fetchone()
    table_comment = table_comment[0] if table_comment else ""
    
    # 获取字段信息
    cursor.execute(f"""
        SELECT COLUMN_NAME, COLUMN_TYPE, COLUMN_COMMENT
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s
        ORDER BY ORDINAL_POSITION
    """, (database, table))
    columns = cursor.fetchall()
    
    md = f"## 表名：{table_name}\n"
    md += f"表注释：{table_comment}"
    md += f"| 列名 | 类型 | 注释 |\n"
    md += "|--------|----|------------|\n"
    for column in columns:
        name, type_, comment = column
        type_zh = db_type_to_str(type_)
        comment = comment.replace('|', '#')
        md += f"| {name} | {type_zh} | {comment} |\n"
    
    print(md)
    #print(table_name)
    #print(table_comment)
    #print(columns)
cursor.close()
conn.close()

