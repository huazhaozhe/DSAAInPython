# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/9 15:43
# @Author   : zhe
# @FileName : quicksort.py
# @Project  : PyCharm


def qucik_sort1(lst):
    def qsort_rec(lst, l, r):
        if l >= r:
            return
        i = l
        j = r
        pivot = lst[i]
        while i < j:
            while i < j and lst[j] >= pivot:
                j -= 1
            if i < j:
                lst[i] = lst[j]
                i += 1
            while i < j and lst[i] <= pivot:
                i += 1
            if i < j:
                lst[j] = lst[i]
                j -= 1
        lst[i] = pivot
        qsort_rec(lst, l, i - 1)
        qsort_rec(lst, i + 1, r)

    qsort_rec(lst, 0, len(lst) - 1)
