# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Higher-order-function.py
   Author :        LiSen
   Date：          2018/8/1 22:18:
-------------------------------------------------
"""
from functools import reduce

# 函数本身也可以赋值给变量，即：变量可以指向函数。
# 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数

# map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
# map()可以接受多个序列，但必须保证每个序列长度相等，区别zip()的木桶原理。


def f(x):
    return x * x


a = map(f, [1, 2, 3, 4, 5])
print a  # [1, 4, 9, 16, 25]


def f1(x, y):
    return x + y


b = map(f1, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
print b   # [2, 4, 6, 8, 10]

'**********************************************************************************************************************'

# reduce    reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 必须结束两个参数,常用于累计操作。有多个变一个


def fn(x, y):
    return x * 10 + y


print reduce(fn, [1, 2, 3, 4])  # 1234


def char_num(s):
    return {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9}[s]


print reduce(fn, map(char_num, '1357'))


def char2num(s):
    return {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9}[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print str2int('753')


'********************************************************************************************'


# filter()
# filter()接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def not_empty(s):
    return s and s.strip()


print filter(not_empty, ['a', '', 'b', '', 'c'])


class A(object):
    count = 0

    def __init__(self, name):
        self.name = name
        A.count += 1
