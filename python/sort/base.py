import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print '%s cost: %s sec' %(func.__name__, round(end - start, 4))
        return result
    return wrapper

def swap(arr, a, b):
    if arr and a < len(arr) and b < len(arr):
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def print_arr(arr):
    for i in arr:
        print '%d ' %i,
    print
