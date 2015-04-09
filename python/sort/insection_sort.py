#!/usr/bin/env python

import base
from base import timeit

@timeit
def insertion_sort(arr):
    rtn = []

    for i in arr:
        rtn = insert(rtn, i)
    return rtn

def insert(sorted_arr, new_ele):
    new_arr = [0 for i in range(0, len(sorted_arr)+1)]

    i = 0
    flag = False
    while (i < len(sorted_arr)):
	if sorted_arr[i] < new_ele:
            new_arr[i] = sorted_arr[i]
	    i += 1
	else:
            flag = True
	    new_arr[i] = new_ele
	    break

    if flag:
        new_arr[i+1:] = sorted_arr[i:]
    else:
	new_arr[i] = new_ele

    return new_arr

@timeit
def insertion_sort2(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            p = i-1
            t = arr[i]
            arr[i] = arr[i-1]
            while t < arr[p] and p >= 0:
                arr[p+1] = arr[p]
                p -= 1
            arr[p+1] = t
    return arr

def shell_sort(arr, n):
    di = n/2
    while di >=1:
        insertion_sort_base(arr, n, di)
        di = di/2
    return arr

def insertion_sort_base(arr, n, d):
    for i in range(d, n):
        if arr[i] < arr[i-d]:
            p = i-d
            t = arr[i]
            arr[i] = arr[i-d]
            while p >= 0 and t < arr[p]:
                arr[p+d] = arr[p]
                p -= d
            arr[p+d] = t
    return arr

if __name__=='__main__':
    arr = [5, 21, 4, 6, 12, 33, 15, 195, 27, 31, 57]

    base.print_arr(arr)
    #arr = insection_sort2(arr)
    #arr = insertion_sort_base(arr, len(arr), 1)
    arr = shell_sort(arr, len(arr))
    base.print_arr(arr)
