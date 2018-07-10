# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/10 9:24
# @Author   : zhe
# @FileName : merge_sort.py
# @Project  : PyCharm

def merge(lfrom, lto, low, mid, high):
    i, j, k = low, mid, low
    while i < mid and j < high:
        if lfrom[k] <= lfrom[i]:
            lto[k] = lfrom[i]
            i += 1
        else:
            lto[k] = lfrom[j]
            j += 1
        k += 1
    while i < mid:
        lto[k] = lfrom[i]
        i += 1
        k += 1
    while j < high:
        lto[k] = lfrom[j]
        j += 1
        k += 1


def merge_pass(lfrom, lto, llen, slen):
    i = 0
    while i + 2 * slen < llen:
        merge(lfrom, lto, i, i + slen, i + 2 * slen)
        i += 2 * slen
    if i + slen < llen:
        merge(lfrom, lto, i, i+slen, llen)
    else:
        for j in range(i, llen):
            lto[j] = lfrom[j]


def merge_sort(lst):
    slen, llen = 1, len(lst)
    temp = [None] * llen
    while slen < llen:
        merge_pass(lst, temp, llen, slen)
        slen *= 2
        merge_pass(temp, lst, llen, slen)
        slen *= 2
