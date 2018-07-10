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


def quick_sort2(lst):
    def qsort(lst, begin, end):
        if begin >= end:
            return
        pivot = lst[begin]
        i = begin
        for index in range(begin + 1, end + 1):
            if lst[index] < pivot:
                i += 1
                lst[i], lst[index] = lst[index], lst[i]
        lst[begin], lst[i] = lst[i], pivot
        qsort(lst, begin, i - 1)
        qsort(lst, i + 1, end)

    qsort(lst, 0, len(lst) - 1)
