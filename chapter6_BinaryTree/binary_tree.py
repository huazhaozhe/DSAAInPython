# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/5 8:56
# @Author   : zhe
# @FileName : binary_tree.py
# @Project  : PyCharm


def BinTree(data, left=None, right=None):
    return [data, left, right]


def is_empty_BinTree(btree):
    return btree is None


def root(btree):
    return btree[0]


def left(btree):
    return btree[1]


def right(btree):
    return btree[2]


def set_root(btree, data):
    btree[0] = data


def set_left(btree, left):
    btree[1] = left


def set_right(btree, right):
    btree[2] = right


def make_sum(a, b):
    return ('+', a, b)


def make_diff(a, b):
    return ('-', a, b)


def make_prod(a, b):
    return ('*', a, b)


def make_div(a, b):
    return ('/', a, b)


def is_basic_exp(a):
    return not isinstance(a, tuple)


def is_number(x):
    return isinstance(x, int) or isinstance(x, float) or isinstance(x, complex)


def eval_sum(a, b):
    if is_number(a) and is_number(b):
        return a + b
    if is_number(a) and a == 0:
        return b
    if is_number(b) and b == 0:
        return a
    return make_sum(a, b)


def eval_diff(a, b):
    if is_number(a) and is_number(b):
        return a - b
    if is_number(a) and a == 0:
        return -b
    if is_number(b) and b == 0:
        return a
    return make_diff(a, b)


def eval_prod(a, b):
    if is_number(a) and is_number(b):
        return a * b
    if is_number(a) and a == 0:
        return 0
    if is_number(b) and b == 0:
        return 0
    return make_prod(a, b)


def eval_div(a, b):
    if is_number(b) and b == 0:
        raise ZeroDivisionError
    if is_number(a) and is_number(b):
        return a / b
    if is_number(a) and a == 0:
        return 0
    return make_div(a, b)


def eval_exp(e):
    if is_basic_exp(e):
        return e
    op, a, b = e[0], eval_exp(e[1]), eval_exp(e[2])
    if op == '+':
        return eval_sum(a, b)
    elif op == '-':
        return eval_diff(a, b)
    elif op == '*':
        return eval_prod(a, b)
    elif op == '/':
        return eval_div(a, b)
    else:
        raise ValueError('Unknown operator:', op)


class PrioQueueError(ValueError):
    pass


class PrioQue():
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)

    def qbqueue(self, e):
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i + 1, e)

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in peek')
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in dequeue')
        return self._elems.pop()


class PrioQueue():
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in peek')
        return self._elems[0]

    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems) - 1)

    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last - 1) // 2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in dequeue')
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0

    def sifdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, j * 2 + 1
        elems[i] = e


class BinTNode():

    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right

def count_BinTNode(t):
    if t is None:
        return 0
    else:
        return 1+count_BinTNode(t.left) + count_BinTNode(t.right)

def sum_BinTNode(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BinTNode(t.left) + sum_BinTNode(t.right)

def preorder(t, proc):
    '''
    先根序遍历
    :param t: 二叉树类BinTNode
    :param proc: 节点数据操作
    :return: 返回None
    '''
    if t is None:
        return
    proc(t.data)
    preorder(t.left, proc)
    preorder(t.right, proc)

def print_BinTNodes(t):
    if t is None:
        print('^', end='')
        return
    print('('+str(t.data), end='')
    print_BinTNodes(t.left)
    print_BinTNodes(t.right)
    print(')', end='')


from chapter5_StackAndQueue.queue import *

def levelorder(t, proc):
    '''
    宽度优先遍历
    :param t: 二叉树
    :param proc: 节点数据操作
    :return: 返回None
    '''
    qu = Squeue()
    qu.enqueue(t)
    while not qu.is_empty():
        n = qu.dequeue()
        if t is None:
            continue
        qu.enqueue(t.left)
        qu.enqueue(t.right)
        proc(t.data)

from chapter5_StackAndQueue.stack import *

def preorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            proc(t.data)
            s.push(t.right)
            t = t.left
        t = s.pop()


def preorder_elements(t):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right)
            yield t.data
            t = t.left
        t = s.pop()