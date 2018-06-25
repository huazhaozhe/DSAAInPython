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
            raise StackUnderflow('In SStack.top: stack is empty')
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackUnderflow('In SStack.pop: stack is empty')
        return self._elems.pop()


from chapter3_LinearList.node import *

class LStack():

    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self.is_empty():
            raise StackUnderflow('In LStack.top: stack is empty')
        return self._top.get_elem()

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self.is_empty():
            raise StackUnderflow('In LStack.pop: stack is empty')
        p = self._top
        self._top = self._top.get_next()
        return p.get_elem()
