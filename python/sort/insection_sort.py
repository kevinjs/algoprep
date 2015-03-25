#!/usr/bin/env python

import base
from base import timeit

@timeit
def insection_sort(arr):
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

if __name__=='__main__':
    arr = [5, 21, 4, 6, 12, 33, 15, 195, 27, 31, 57]

    base.print_arr(arr)
    arr = insection_sort(arr)
    base.print_arr(arr)
