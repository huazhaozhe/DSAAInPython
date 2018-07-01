# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : zhe
# @File     : test.py
# @Time     : 2018/07/01 20:52
# @Software : PyCharm


from .stack import check_parens, trans_infix_suffix, suf_exp_evalustor


def test_trans_infix_suffixs(s):
    print(s)
    check = check_parens(s)
    assert check['match'] is True
    correct_value = eval(s)
    tran = trans_infix_suffix(s)
    print(tran)
    value = suf_exp_evalustor(' '.join(tran))
    print(correct_value, value)
    assert correct_value == value
