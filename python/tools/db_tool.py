import pymysql
from pyhive import presto


def mysql_connect():
    '''
    MySQL连接
    '''
    return pymysql.connect(
        host = 'localhost',
        user = 'dev',
        password = 'Dotw@2024',
        database = 'test',
        charset = 'utf8mb4'
    )


def mysql_connect():
    '''
    Presto连接
    '''
    presto_conn = presto.connect(
        host = 'emr-bi',
        port = 9090,
        catalog='hive',
        schema='default'
    )

    return presto_conn.cursor()