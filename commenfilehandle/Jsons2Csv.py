#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created with pycharm.
# User: sssd
# Date: 2017/12/29 11:26
# Version: V1.0
# To change this template use File | Settings | File Templates.
# Description:   python 实现 json 的 txt 文件保存为 .csv 文件 （注意；其中有空行的bug暂时还没有解决）

__author__ = 'sssd'

import json
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
f = open("C:\\Users/sssd/Desktop/f2.txt","r")
temp = '['
lines = f.readlines()
for line in lines:
    tempValue = line.replace("\n","") + ","
    temp += tempValue
json_str = temp[:-1] + ']'
print json_str
# json_str = '[{"a":1,"b":"2","c":"3","d":{"d1":"4"}},{"a":21,"c":"23","d":{"d1":"24"},"e":"25"}]'

o = json.loads(json_str)

def loop_data(o, k=''):
    global json_ob, c_line
    if isinstance(o, dict):
        for key, value in o.items():
            if(k==''):
                loop_data(value, key)
            else:
                loop_data(value, k + '.' + key)
    elif isinstance(o, list):
        for ov in o:
            loop_data(ov, k)
    else:
        if not k in json_ob:
            json_ob[k]={}
        json_ob[k][c_line]=o

def get_title_rows(json_ob):
    title = []
    row_num = 0
    rows=[]
    for key in json_ob:
        title.append(key)
        v = json_ob[key]
        if len(v)>row_num:
            row_num = len(v)
        continue
    for i in range(row_num):
        row = {}
        for k in json_ob:
            v = json_ob[k]
            if i in v.keys():
                row[k]=v[i]
            else:
                row[k] = ''
        rows.append(row)
    return title, rows

def write_csv(title, rows, csv_file_name):
    with open(csv_file_name, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=title)
        writer.writeheader()
        writer.writerows(rows)

def json_to_csv(object_list):
    global json_ob, c_line
    json_ob = {}
    c_line = 0
    for ov in object_list :
        loop_data(ov)
        c_line += 1
    title, rows = get_title_rows(json_ob)
    write_csv(title, rows, 'test.csv')

if __name__ == '__main__':
    json_to_csv(o)
