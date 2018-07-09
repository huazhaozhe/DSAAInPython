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
        while j > 0 and lst[j - 1] > value:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = value


def select_sort(lst):
    '''
    选择排序
    :param lst: 同insert_sort
    :return: 同insert_sort
    '''
    for i in range(len(lst) - 1):
        index = i
        for j in range(i, len(lst)):
            if lst[j] < lst[index]:
                index = j
        if lst[index] < lst[i]:
            lst[i], lst[index] = lst[index], lst[i]
