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
    不稳定举例: [5, 8, 5, 2, 9],第一个5和第二个5
    改变交换的方式,比如和插入排序一后移可以使其稳定
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


def hubble_sort1(lst):
    '''
    交换排序: 冒泡法
    :param lst: 同insert_sort
    :return: 同insert_sort
    '''

    count = len(lst) - 1
    while count > 0:
        found = False
        for i in range(count):
            if lst[i + 1] < lst[i]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                found = True
        if not found:
            break
        count -= 1