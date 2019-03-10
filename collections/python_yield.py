# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     python_yield.py
   Author :        LiSen
   Date：          2018/8/1 21:26:
-------------------------------------------------
"""
# 1.斐波那契数列


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n += 1


# fab(5)   # 1 1 2 3 5
'直接在 fab 函数中用 print 打印数字会导致该函数可复用性较差，因为 fab 函数返回 None，其他函数无法获得该函数生成的数列。'

# 改进1


def fab(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n += 1
    return L

# for i in fab(5):
#     print i


'该函数在运行中占用的内存会随着参数 max 的增大而增大，如果要控制内存占用，最好不要用 List来保存中间结果，而是通过 iterable 对象来迭代。'


# 改进2

class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()
# a = Fab(5)
# print a.next()
# print a.next()
# print a.next()
# print type(a)
# for i in a:
#     print i
# 此时代码显得不够简洁

# 改进3 使用yield


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1


a = fab(5)
print a.next()
print type(a)    # <type 'generator'>
for i in fab(5):
    print i


# 总结
'''
fab 和 fab(5)，fab 是一个 generator function，而 fab(5) 是调用 fab 返回的一个 generator，
yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，
调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，
fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，
于是函数继续执行，直到再次遇到 yield。当函数执行结束时，generator 自动抛出 StopIteration 异常，表示迭代完成。
在 for 循环里，无需处理 StopIteration 异常，循环会正常结束。

一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，
直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，
并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，
每次中断都会通过 yield 返回当前的迭代值。
在一个 generator function 中，如果没有 return，则默认执行至函数完毕，如果在执行过程中 return，则直接抛出 StopIteration 终止迭代。
'''


# 在文件读取时，如果直接对文件对象调用 read() 方法，会导致不可预测的内存占用。
# 好的方法是利用固定长度的缓冲区来不断读取文件内容。通过 yield返回，我们不再需要编写读文件的迭代类，就可以轻松实现文件读取：

def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as fp:
        block = fp.read(BLOCK_SIZE)
        if block:
            yield block
        else:
            return

