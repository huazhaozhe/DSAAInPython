# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/5 8:56
# @Author   : zhe
# @FileName : binary_tree.py
# @Project  : PyCharm


def bin_tree(data, left=None, right=None):
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

