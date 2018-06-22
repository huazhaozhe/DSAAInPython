# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/6/22 8:31
# @Author   : zhe
# @FileName : Josephue.py
# @Project  : PyCharm

from .CList import *


def josephus_A(n, k, m):
    people = list(range(1, n + 1))
    i = k - 1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end='')
                people[i] = 0
            i = (i + 1) % n
        if num == n-1:
            print('')
        else:
            print(', ', end='')

