#!/usr/bin/env python

import base
from base import timeit

@timeit
def counting_sort(arr):
    arr_max = max(arr)
    arr_min = min(arr)

    c_arr = [0 for i in range(0, arr_max-arr_min+1)]
    t_arr = [0 for i in range(0, len(arr))]

    for i in arr:
        c_arr[i-arr_min] += 1

    for i in range(0, len(c_arr)-1):
        c_arr[i+1] += c_arr[i]

    for i in arr[::-1]:
        c_arr[i-arr_min] -= 1
        t_arr[c_arr[i-arr_min]] = i
    return t_arr

if __name__=='__main__':
    arr = [5,21,4,-6,12,33,15]

    base.print_arr(arr)
    arr = counting_sort(arr)
    base.print_arr(arr)
