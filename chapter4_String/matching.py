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


def matching_KMP(t, p):
    n, m = len(t), len(p)
    i, k = 0, -1
    pnext = [-1] * m  # 初始数组全为-1
    while i < m - 1:  # 生成下一个pnext元素值
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            pnext[i] = k  # 设置pnext元素
        else:
            k = pnext[k]  # 退到更短相同前缀

    i, j = 0, 0

    '''
    # 展开
    while j < n and i < m:             # i==m找到匹配
        if i == -1:                    # 遇到-1,比较下一对字符
            j, i = j + 1, i + 1
        elif t[j] == p[i]:             # 字符相等,比较下一对字符
            j, i = j + 1, i + 1
        else:
            i = pnext[i]               # 匹配失败,从pnext取得p的下一字符位置
    '''

    result = {'count': 0, 'index': []}
    while j < n - m - 1:
        i = 0
        while j < n and i < m:
            if i == -1 or t[j] == p[i]:
                j, i = j + 1, i + 1
            else:
                i = pnext[i]
        if i == m:                      # 匹配成功,返回下标
            result['count'] += 1
            result['index'].append(j - m)
            j = j - m + 1               # j指向匹配成功的下一位,此方法有待改进
    return result
