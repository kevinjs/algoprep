#!/usr/bin/env python
import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        rtn = func(*args, **kwargs)
        end = time.time()
        print '%s cost time: %s s' %(func.__name__, end - start)
        return rtn
    return wrapper

def cacheit(func):
    cache = {}
    miss = object()

    @wraps(func)
    def wrapper(*args, **kwargs):
        rtn = cache.get(args, miss)
        if rtn is miss:
            rtn = func(*args, **kwargs)
            cache[args] = rtn
        return rtn
    return wrapper

def fib_1(n):
    if n < 2:
        return n
    return fib_1(n-1) + fib_1(n-2)

@cacheit
def fib_2(n):
    if n < 2:
        return n
    return fib_2(n-1) + fib_2(n-2)

@timeit
def call_1(n):
    print fib_1(n)

@timeit
def call_2(n):
    print fib_2(n)

if __name__=='__main__':
    call_2(60)
    call_1(60)
