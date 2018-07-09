# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/9 13:50
# @Author   : zhe
# @FileName : simple_sorting_algorithm.py
# @Project  : PyCharm


def insert_sort(lst):
    '''
    插入排序
    :param lst: 待排序的list
    :return: 这里直接修改待排序的list,不需要返回
    '''
    for i in range(1, len(lst)):
        value = lst[i]
        j = i
        while j > 0 and lst[j-1] > value:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = value

