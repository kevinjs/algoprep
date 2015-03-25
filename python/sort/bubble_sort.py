#!/usr/bin/env python

import base
from base import timeit

@timeit
def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                base.swap(arr, j, j+1)

if __name__=='__main__':
    arr = [5, 21, 4, 6, 12, 33, 15, 195, 27, 31, 57]

    base.print_arr(arr)
    bubble_sort(arr)
    base.print_arr(arr)
