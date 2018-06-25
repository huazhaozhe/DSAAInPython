# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/6/25 14:06
# @Author   : zhe
# @FileName : stack.py
# @Project  : PyCharm


class StackUnderflow(ValueError):
    pass

class SStack():

    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self.is_empty():
            raise StackUnderflow('stack is empty')
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackUnderflow('stack is empty')
        return self._elems.pop()
