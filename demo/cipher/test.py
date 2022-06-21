#!/usr/bin/python
# coding:utf-8

from pyDes import des, PAD_PKCS5, ECB
import base64


DES_SECRET_KEY = "test*key*"


def des_encrypt(str_):

    encrypt_str = str_.encode()
    des_obj = des(DES_SECRET_KEY, ECB, DES_SECRET_KEY, padmode=PAD_PKCS5)
    secret_bytes = des_obj.encrypt(encrypt_str)
    base64_str = base64.b64encode(secret_bytes).decode()
    return base64_str


def des_decrypt(base64_str):
    des_obj = des(DES_SECRET_KEY, ECB, DES_SECRET_KEY, padmode=PAD_PKCS5)
    if len(base64_str) % 2 != 0:    # 要是不能被整除,需要在加密base64字符串后加个=号，要不问为什么，就是这么规定的，要不有时会报错
        base64_str = base64_str + '='
    else:
        base64_str = base64_str + '=='
    base64_types = base64_str.encode()
    secret_bytes = base64.b64decode(base64_types)
    return des_obj.decrypt(secret_bytes).decode()


a = des_encrypt('{"aaa": 这是一个测试}')
b = des_decrypt(a)
print('a', type(a), a)
print('b', type(b), b)
