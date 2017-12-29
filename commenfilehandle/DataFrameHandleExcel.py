#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created with pycharm.
# User: sssd
# Date: 2017/12/29 11:29
# Version: V1.0
# To change this template use File | Settings | File Templates.
# Description:  python pandas 实现 对 excel 的相关操作

__author__ = 'sssd'

import pandas as pd

# 返回变化
def ischange(s):
    return s == u'\u53d8\u5316'

def test():
    df = pd.read_excel('C:\\Users/sssd/Desktop/biao2.xlsx')
    df2 = pd.read_excel('C:\\Users/sssd/Desktop/biao1.xlsx')
    writer = pd.ExcelWriter('C:\\Users/sssd/Desktop/out.xlsx')
    count = 0
    for s in df.icol(3):
        count += 1
        if ischange(s) and df.iat[count - 1, 4] != df.iat[count - 1, 0]:
            urn = df.iat[count - 1, 4]
            list = df2.icol(0).tolist()
            try:
                index = list.index(urn)
                df.iat[count - 1, 5] = df.iat[count - 1, 1] + df2.iat[index, 1]
            except Exception, e:
                df.iat[count - 1, 5] = df.iat[count - 1, 1]
                continue
                # index = df2.icol[:,0].to_string.IndexOf(s)
        else:
            df.iat[count - 1, 5] = df.iat[count - 1, 1]
    df.to_excel(writer, 'Sheet1', )
    writer.save()

if __name__ == '__main__':
    test()
    pass
