#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : zhe
# @File    : linear_link.py
# @Time    : 2018/05/07 19:57
# @Software: PyCharm

import random

class LinkedListUnderflow(ValueError):
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
        return self._elem

    def set_next(self, next=None):
        self._next = next
        if next:
            return self._next.get_elem()
        else:
            return None

    def __str__(self):
        return 'elem: ' + str(self._elem) + '\tnext: ' + str(self._next)

    __repr__ = __str__


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
            raise LinkedListUnderflow('in pop')
        e = self._head
        self._head = self._head.get_next()
        return e.get_elem()

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
            raise LinkedListUnderflow('in pop_last')
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
                elem_list.append((i, p.get_elem()))
            i += 1
            p = p.get_next()
        return elem_list

    def filter(self, pred):
        p = self._head
        while p is not None:
            elem = p.get_elem()
            if pred(elem):
                yield elem
            p = p.get_next()

    def for_each(self, proc):
        p = self._head
        while p is not None:
            proc(p.get_elem())
            p = p.get_next()

    def elements(self):
        p = self._head
        while p is not None:
            yield p.get_elem()
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
        if self.length() > 1:
            length = self.length()
            for i in range(length // 2):
                tmp1 = None
                tmp2 = None
                p = self._head
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
        LList.__init__(self)
        self._rear = None

    def prepend(self, elem=None):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem=None):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.set_next(LNode(elem))
            self._rear = self._rear.get_next()

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow
        e = self._head
        self._head = self._head.get_next()
        if self._head is None:
            self._rear = self._head
        return e.get_elem()

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
        return e.get_elem()

    def set_empty(self):
        self._head = None
        self._rear = None



# 循环单链表
class LCList:

    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

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

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow('in pop of CLList')
        p = self._rear.get_next()
        if self._rear is p:
            self._rear = None
        else:
            self._rear.set_next(p.get_next())
        return p

    def printall(self):
        if self._rear is None:
            print('empty list')
        else:
            # 单个结点
            if self._rear is self._rear.get_next():
                print(self._rear.get_elem())
            else:
                # p = self._rear.get_next()
                # i = 1
                # while True:
                #     print(i, '-', p.get_elem())
                #     p = p.get_next()
                #     if p is self._rear.get_next():
                #         break
                #     i += 1

                p = self._rear.get_next()
                i = 1
                while True:
                    print(i, '-', p.get_elem())
                    if p is self._rear:
                        break
                    p = p.get_next()
                    i += 1


# 添加反向引用
class DLNode(LNode):
    def __init__(self, elem=None, prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev

    def get_prev(self):
        return self.prev

    def set_prev(self, prev=None):
        self.prev = prev
        if prev:
            return self.prev.get_elem()
        else:
            return None

# 双链表
class DLList(LList1):
    def __init__(self):
        LList1.__init__(self)

    def prepend(self, elem=None):
        if self._head is None:
            self._head = DLNode(elem)
            self._rear = self._head
        else:
            self._head = DLNode(elem, next_=self._head)
            self._head.get_next().set_prev(self._head)
        return self._head.get_elem()

    def append(self, elem=None):
        if self._head is None:
            self._head = DLNode(elem)
            self._rear = self._head
        else:
            self._rear = DLNode(elem, self._rear)
            self._rear.get_prev().set_next(self._rear)
        return self._rear.get_elem()

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow
        e = self._head
        self._head = self._head.get_next()
        if self._head is None:
            self._rear = self._head
        else:
            self._head.set_prev()
        return e.get_elem()

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow
        e = self._rear
        self._rear = self._rear.get_prev()
        if self._rear is None:
            self._head = None
        else:
            self._rear.set_next()
        return e.get_elem()

class DCList():
    def __init__(self):
        self._head = None

    def prepend(self, elem=None):
        if self._head is None:
            self._head = DLNode(elem)
            self._head.set_next(self._head)
            self._head.set_prev(self._head)
        else:
            self._head = DLNode(elem, self._head.get_prev(), self._head)
            self._head.get_prev().set_next(self._head)
            self._head.get_next().set_prev(self._head)
        return self._head.get_elem()

    def append(self, elem=None):
        self.prepend(elem)
        self._head = self._head.get_next()
        return self._head.get_elem()

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow
        p = self._head
        if self._head is p.get_next():
            self._head = None
        else:
            self._head = p.get_next()
            self._head.set_prev(p.get_prev())
            p.get_prev().set_next(self._head)
        return p.get_elem()

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow
        p = self._head.get_prev()
        if self._head is p:
            self._head = None
        else:
            self._head.set_prev(p.get_prev())
            p.get_prev().set_next(self._head)
        return p.get_elem()

    def length(self):
        if self._head is None:
            return 0
        p = self._head
        i = 1
        while p.get_next() is not self._head:
            i += 1
            p = p.get_next()
        return i

    def printall(self):
        if self._head is None:
            return 'DCList list is empty'
        i = 1
        p = self._head
        while True:
            print(i, ' - ', p.get_elem())
            p = p.get_next()
            if p is self._head:
                break
            i += 1