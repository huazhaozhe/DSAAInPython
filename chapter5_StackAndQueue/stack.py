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


def check_parens(text):
    '''括号匹配检查函数， text为被检查的字符串'''
    open_parens = '([{'
    close_parens = ')]}'
    i, text_len = 0, len(text)
    st = SStack()
    result = {'match': False, 'count': 0}
    while i < text_len:
        if text[i] in open_parens:
            st.push((i, text[i]))
        elif text[i] in close_parens:
            if not st.is_empty() and open_parens.index(
                    st.pop()[1]) == close_parens.index(text[i]):
                result['count'] += 1
            else:
                break
        i += 1
    if i < text_len:
        print('Unmatching is found at', i, 'for', text[i])
    elif i == text_len and not st.is_empty():
        print('Unmatching is found at', st.top()[0], 'for', st.top()[1])
    elif result['count'] == 0:
        print('No found parens')
    elif i == text_len and result['count'] > 0 and st.is_empty():
        print('All pass')
        result['match'] = True
    return result


class ESStack(SStack):

    def depath(self):
        return len(self._elems)


def suf_exp_evalustor(exp):
    operators = '+-*/'
    st = ESStack()
    for x in exp:
        if x not in operators:
            st.push(float(x))
            continue
        if st.depath() < 2:
            raise SyntaxError('Short of operand(s).')
        b = st.pop()
        a = st.pop()
        if x == '+':
            c = a + b
        elif x == '-':
            c = a - b
        elif x == '*':
            c = a * b
        elif x == '/':
            if b == 0:
                raise ZeroDivisionError('division by zero')
            c = a / b
        st.push(c)
    if st.depath() == 1:
        return st.pop()
    raise SyntaxError('Extra operand(s).')


def trans_infix_suffix(line):
    operators = '+-*/()'
    property = {'(': 1, '+': 3, '-': 3, '*': 5, '/': 5}
    st = SStack()
    exp = []
    line = line.split()
    for x in line:
        if x == '(':
            st.push(x)
        elif x == ')':
            while st.top() != '(':
                exp.append(st.pop())
            try:
                st.pop()
            except:
                raise SyntaxError("Missing '('.")
        elif x not in operators:
            exp.append(x)
        else:
            while not st.is_empty() and property[st.top()] >= property[x]:
                exp.append(st.pop())
            st.push(x)
    while not st.is_empty():
        if st.top() == '(':
            raise SyntaxError("Extra '('.")
        exp.append(st.pop())
    return exp


def norec_fact(n):
    res = 1
    st = SStack()
    while n > 0:
        st.push(n)
        n -= 1
    while not st.is_empty():
        res *= st.pop()
    return res

