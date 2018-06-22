# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/6/21 15:11
# @Author   : zhe
# @FileName : node.py
# @Project  : PyCharm


class LinkedListUnderflow(Exception):
    pass

# 结点
class LNode:
    def __init__(self, elem=None, next_=None):
        self._elem = elem
        self._next = next_

    def get_elem(self):
        return self._elem

    def get_next(self):
        return self._next

    def set_elem(self, elem=None):
        self._elem = elem

    def set_next(self, next=None):
        self._next = next

# 添加反向引用
class DLNode(LNode):
    def __init__(self, elem=None, prev=None, next_=None):
        super().__init__(elem, next_)
        self.prev = prev

    def get_prev(self):
        return self.prev

    def set_prev(self, prev=None):
        self.prev = prev
