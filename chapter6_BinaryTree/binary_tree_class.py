# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/9 13:13
# @Author   : zhe
# @FileName : binary_tree_class.py
# @Project  : PyCharm


class BinTNode():

    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right


def count_BinTNode(t):
    if t is None:
        return 0
    else:
        return 1 + count_BinTNode(t.left) + count_BinTNode(t.right)


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
    print('(' + str(t.data), end='')
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
    qu = SQueue(10)
    qu.enqueue(t)
    while not qu.is_empty():
        t = qu.dequeue()
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


def postorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left if t.left is not None else t.right
        t = s.pop()
        proc(t.data)
        if not s.is_empty() and t is s.top().left:
            # 左子结点遍历完成,遍历右子结点
            t = s.top().right
        elif not s.is_empty() and t is s.top().right:
            # 右子结点遍历完成,下一步是弹出父结点
            # 将t设为None防止子结点再次入栈再次遍历一遍下面的子结点(退栈)
            t = None
        else:
            # 根节点,退栈
            t = None
        '''
        可以合并为:
        else:
            t = None
        '''


class BinTreeError(ValueError):
    pass


class BinTree():

    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def root(self):
        return self._root

    def leftchild(self):
        if self.is_empty():
            raise BinTreeError('BinTree is None')
        return self._root.left

    def rightchild(self):
        if self.is_empty():
            raise BinTreeError('BinTree is None')
        return self._root.righr

    def set_root(self, rootnode):
        self._root = rootnode

    def set_left(self, leftnode):
        if self.is_empty():
            raise BinTreeError()
        self._root.left = leftnode

    def set_right(self, rightnode):
        if self.is_empty():
            raise BinTreeError()
        self._root.righr = rightnode

    def preorder_elements(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t.right)
                yield t.data
                t = t.left
            t = s.pop()
