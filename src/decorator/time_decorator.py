#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    des: 装饰器，调用函数之前打印调用函数的时间
    author: leslieyuan
    time: 2021-02-07 10：59
    version:
"""

import time

def TimeDecorator(allFunction):
    def Decorator(*args, **kwargs):
        print 'Function "%s" call time is %s' % (allFunction.__name__, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return allFunction(*args, **kwargs)
    return Decorator


@TimeDecorator
def TestFunc():
    print "TestFunc entry"


if __name__ == '__main__':
    print 'Main function entry'
    TestFunc()