# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/6/22 14:03
# @Author   : zhe
# @FileName : matching.py
# @Project  : PyCharm


def naive_matching(t, p):
    m, n = len(p), len(t)
    result = {'count': 0, 'index': []}
    for i in range(n - m + 1):
        count = 0
        for j in range(m):
            if t[i + j] == p[j]:
                count += 1
            else:
                break
        if count == m:
            result['count'] += 1
            result['index'].append(i)
    return result
