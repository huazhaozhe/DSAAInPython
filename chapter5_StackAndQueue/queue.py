# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/3 18:37
# @Author   : zhe
# @FileName : queue.py
# @Project  : PyCharm

class QueueUnderflow(ValueError):
    pass

class Squeue():
    '''
    队列的list实现
    '''
    def __init__(self, init_len=0):
        self._len = init_len
        self._eleme = [0] * init_len
        self._head = 0
        self._num = 0

    def is_empty(self):
        return self._num == 0

    def peek(self):
        if self._num == 0:
            raise QueueUnderflow('in peek')
        return self._eleme[self._head]

    def dequeue(self):
        if self._num == 0:
            raise QueueUnderflow('in dequeue')
        e = self._eleme[self._head]
        self._head = (self._head+1) % self._len
        self._num -= 1
        return e

    def enqueue(self, e):
        if self._num == self._len:
            self.__extend()
        self._eleme[(self._head+self._num) % self._len] = e
        self._num += 1

    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elem = [0]*self._len
        for i in range(old_len):
            new_elem[i] = self._eleme[(self._head+i) % old_len]
        self._eleme, self._head = new_elem, 0
