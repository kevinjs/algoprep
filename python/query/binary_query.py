#!/usr/bin/env python
from base import timeit
import math

def binary_query(arr, st, ed, target):
    #import pdb;pdb.set_trace()
    if st == ed:
        if arr[st] == target:
            return True, st
        else:
            return False, -1

    half = int(math.floor((ed + st)/2))

    if target == arr[half]:
        return True, half
    else:
        if target > arr[half]:
            return binary_query(arr, half+1, ed, target)
        else:
            return binary_query(arr, st, half-1, target)

@timeit
def run(arr, st, ed, target):
    return binary_query(arr, st, ed, target)

if __name__=='__main__':
    sorted_arr = [-88, 4, 5, 6, 11, 12, 15, 21, 27, 31,33, 57, 195]
    print run(sorted_arr, 0, len(sorted_arr) ,32)
