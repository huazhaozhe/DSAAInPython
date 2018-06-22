# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/6/21 15:21
# @Author   : zhe
# @FileName : LList.py
# @Project  : PyCharm

from .node import LNode, DLNode, LinkedListUnderflow

# 实现单链表
class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def set_empty(self):
        self._head = None

    def prepend(self, elem=None):
        self._head = LNode(elem, self._head)
        return self._head

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop of LList')
        e = self._head
        self._head = self._head.get_next()
        return e

    def append(self, elem=None):
        if self._head is None:
            self._head = LNode(elem)
            return self._head
        p = self._head
        while p.get_next() is not None:
            p = p.get_next()
        p.set_next(LNode(elem))
        return p.get_next()

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_last of LList')
        p = self._head
        if p.get_next() is None:
            self._head = None
            return p
        while p.get_next().get_next() is not None:
            p = p.get_next()
        e = p.get_next()
        p.set_next()
        return e

    def length(self):
        p, n = self._head, 0
        while p is not None:
            p = p.get_next()
            n += 1
        return n

    def find(self, pred):
        i = 0
        p = self._head
        elem_list = []
        while p is not None:
            if p.get_elem() == pred:
                elem_list.append((i, p))
            i += 1
            p = p.get_next()
        return elem_list

    def filter(self, pred):
        p = self._head
        while p is not None:
            elem = p.get_elem()
            if pred(elem):
                yield p
            p = p.get_next()

    def for_each(self, proc):
        p = self._head
        while p is not None:
            p.set_elem(proc(p.get_elem()))
            p = p.get_next()

    def elements(self):
        p = self._head
        while p is not None:
            yield p
            p = p.get_next()

    def printall(self):
        p = self._head
        i = 0
        while p is not None:
            print(i, '-', p.get_elem(), end='')
            if p.get_next() is not None:
                print(', ', end='')
            p = p.get_next()
            i += 1
        print('')

    def reverse(self):
        length = self.length()
        if length > 1:
            for i in range(length // 2):
                p = self._head
                # 初始化j,因为for循环不一定会执行,否则导致j未定义错误
                j = 0
                for j in range(1, i+1):
                    p = p.get_next()
                tmp1 = p.get_elem()
                for j in range(j+1, length-i):
                    p = p.get_next()
                tmp2 = p.get_elem()
                p.set_elem(tmp1)
                p = self._head
                for j in range(1, i+1):
                    p = p.get_next()
                p.set_elem(tmp2)


# 添加尾结点
class LList1(LList):

    def __init__(self):
        super().__init__()
        self._rear = None

    def prepend(self, elem=None):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)
        return self._head

    def append(self, elem=None):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.set_next(LNode(elem))
            self._rear = self._rear.get_next()
        return self._rear

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow
        e = self._head
        self._head = self._head.get_next()
        if self._head is None:
            self._rear = self._head
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop-last')
        p = self._head
        if p.get_next() is None:
            e = p
            self._head = None
            # self._rear = self._head
            return e

        while p.get_next().get_next() is not None:  # while p.get_next() != self._rear
            p = p.get_next()
        e = p.get_next()
        p.set_next()
        self._rear = p
        return e

    def is_empty(self):
        return self._head is None and self._rear is None

    def set_empty(self):
        super().set_empty()
        self._rear = None


# 双链表
class DLList(LList1):
    def __init__(self):
        super().__init__()

    def prepend(self, elem=None):
        if self._head is None:
            self._head = DLNode(elem)
            self._rear = self._head
        else:
            self._head = DLNode(elem, next_=self._head)
            self._head.get_next().set_prev(self._head)
        return self._head

    def append(self, elem=None):
        if self._head is None:
            self._head = DLNode(elem)
            self._rear = self._head
        else:
            self._rear = DLNode(elem, self._rear)
            self._rear.get_prev().set_next(self._rear)
        return self._rear

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow
        e = self._head
        self._head = self._head.get_next()
        if self._head is None:
            self._rear = self._head
        else:
            self._head.set_prev()
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow
        e = self._rear
        self._rear = self._rear.get_prev()
        if self._rear is None:
            self._head = None
        else:
            self._rear.set_next()
        return e

    def reverse(self):
        length = self.length()
        if length > 1:
            p1 = self._head
            p2 = self._rear
            for i in range(length // 2):
                tmp = p1.get_elem()
                p1.set_elem(p2.get_elem())
                p2.set_elem(tmp)
                p1 = p1.get_next()
                p2 = p2.get_prev()