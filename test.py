#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 22:05
# @Author  : LiuShaoheng


class MyLocker(object):
    def __init__(self):
        print('MyLocker.__init__() called')

    @staticmethod
    def acquire():
        print('MyLocker.acquire() called')

    @staticmethod
    def unlock():
        print('MyLocker.unlock() called')


class LockerEx(MyLocker):
    @staticmethod
    def acquire():
        print('LockerEx.acquire() called')

    @staticmethod
    def unlock():
        print('LockerEx.unlock() called')


def flag(cls):
    def outer(func):
        def inner(*args, **kwargs):
            print('before %s called' % (func.__name__, ))
            cls.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                cls.unlock()
        return inner
    return outer


class Run(object):
    @flag(MyLocker)
    def Func1(self):
        print('Func1 called')

    @flag(MyLocker)
    @flag(LockerEx)
    def Func2(self, a, b):
        print('Func2 called')
        return a + b


if __name__ == '__main__':
    r = Run()
    # r.Func1()
    # print(r.Func1())
    # print(r.Func2(1, 2))
    print(r.Func2(3, 4))














