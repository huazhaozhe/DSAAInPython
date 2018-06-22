# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/6/21 15:17
# @Author   : zhe
# @FileName : CList.py
# @Project  : PyCharm

from .node import LNode, DLNode, LinkedListUnderflow


# 循环单链表
class LCList:

    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def set_empty(self):
        self._rear = None

    def prepend(self, elem):
        if self._rear is None:
            self._rear = LNode(elem, self._rear)
            self._rear.set_next(self._rear)
        else:
            p = LNode(elem, self._rear.get_next())
            self._rear.set_next(p)
        return self._rear.get_next()

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.get_next()
        return self._rear

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow('in pop of LCList')
        p = self._rear.get_next()
        if self._rear is p:
            self._rear = None
        else:
            self._rear.set_next(p.get_next())
        return p

    def length(self):
        p, n = self._rear, 0
        while p is not None:
            n += 1
            p = p.get_next()
            if p is self._rear:
                break
        return n

    def find(self, elem):
        elems_list = []
        if self._rear is not None:
            p, i = self._rear.get_next(), 0
            while True:
                if p.get_elem() == elem:
                    elems_list.append((i, p))
                p = p.get_next()
                if p is self._rear.get_next():
                    break
                i += 1
        return elems_list

    def filter(self, pred):
        if self._rear is not None:
            p = self._rear.get_next()
            while True:
                elem = p.get_elem()
                if pred(elem):
                    yield p
                p = p.get_next()
                if p is self._rear.get_next():
                    break

    def for_each(self, proc):
        p = self._rear
        while p is not None:
            p.set_elem(proc(p.get_elem()))
            p = p.get_next()
            if p is self._rear:
                break

    def elements(self):
        if self._rear is not None:
            p = self._rear.get_next()
            while True:
                yield p
                p = p.get_next()
                if p is self._rear.get_next():
                    break
    def reverse(self):
        length = self.length()
        if length > 1:
            for i in range(length // 2):
                p = self._rear.get_next()
                # 初始化j,因为for循环不一定会执行,否则导致j未定义错误
                j = 0
                for j in range(1, i+1):
                    p = p.get_next()
                tmp1 = p.get_elem()
                for j in range(j+1, length-i):
                    p = p.get_next()
                tmp2 = p.get_elem()
                p.set_elem(tmp1)
                p = self._rear.get_next()
                for j in range(1, i+1):
                    p = p.get_next()
                p.set_elem(tmp2)

    def printall(self):
        if self._rear is None:
            print('empty list')
        else:
            # 单个结点
            if self._rear is self._rear.get_next():
                print(0, '-', self._rear.get_elem())
            else:
                p = self._rear.get_next()
                i = 0
                while True:
                    print(i, '-', p.get_elem())
                    if p is self._rear:
                        break
                    p = p.get_next()
                    i += 1


# 循环双链表
class DCList(LCList):
    def __init__(self):
        super().__init__()

    def prepend(self, elem=None):
        if self._rear is None:
            self._rear = DLNode(elem)
            self._rear.set_next(self._rear)
            self._rear.set_prev(self._rear)
        else:
            p = DLNode(elem, self._rear, self._rear.get_next())
            self._rear.get_next().set_prev(p)
            self._rear.set_next(p)
        return self._rear.get_next()

    def append(self, elem=None):
        self.prepend(elem)
        self._rear = self._rear.get_next()
        return self._rear

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow('in pop of DCList')
        p = self._rear.get_next()
        if self._rear is p:
            self._rear = None
        else:
            p.get_next().set_prev(self._rear)
            self._rear.set_next(p.get_next())
        return p

    def pop_last(self):
        if self._rear is None:
            raise LinkedListUnderflow('in pop_list of DCList')
        p = self._rear
        if self._rear is p.get_next():
            self._rear = None
        else:
            self._rear = p.get_prev()
            self._rear.set_next(p.get_next())
            p.get_next().set_prev(self._rear)
        return p

    def reverse(self):
        length = self.length()
        if length > 1:
            p1 = self._rear.get_next()
            p2 = self._rear
            for i in range(length // 2):
                tmp = p1.get_elem()
                p1.set_elem(p2.get_elem())
                p2.set_elem(tmp)
                p1 = p1.get_next()
                p2 = p2.get_prev()
