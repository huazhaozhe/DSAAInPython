# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/6/22 8:31
# @Author   : zhe
# @FileName : Josephue.py
# @Project  : PyCharm

from .CList import LCList


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
        if num == n - 1:
            print('')
        else:
            print(', ', end='')


def josephus_B(n, k, m):
    people = list(range(1, n + 1))
    i = k - 1
    while people:
        length = len(people)
        i = (i + m - 1) % length
        num = people.pop(i)
        print(num, end=(', ' if length != 1 else '\n'))


class Josephus(LCList):

    def __init__(self, n, k, m):
        super(Josephus, self).__init__()
        self.n = n
        self.k = k
        self.m = m
        for i in range(1, self.n + 1):
            self.append(i)

    def turn(self, m):
        for i in range(m):
            self._rear = self._rear.get_next()

    def run(self):
        self.turn(self.k - 1)
        while not self.is_empty():
            self.turn(self.m - 1)
            num = self.pop()
            print(num.get_elem(),
                  end=(', ' if self.length() != 0 else '\n'))
