#!/usr/bin/env python

import base
from base import timeit

@timeit
def selection_sort(arr):
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                base.swap(arr, i, j)

if __name__=='__main__':
    arr = [5, 21, 4, 6, 12, 33, 15, 195, 27, 31, 57]

    base.print_arr(arr)
    selection_sort(arr)
    base.print_arr(arr)
