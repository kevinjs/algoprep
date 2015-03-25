#!/usr/bin/env python

import base
from base import timeit

def partition(arr, left, right, pivot):
    pivot_value = arr[pivot]
    base.swap(arr, pivot, right)

    new_pivot = left

    for i in range(left, right):
        if arr[i] <= pivot_value:
            base.swap(arr, new_pivot, i)
            new_pivot += 1
    base.swap(arr, new_pivot, right)

    return new_pivot

def quick_sort(arr, left, right):
    if left < right:
        pivot = left
        new_pivot = partition(arr, left, right, pivot)
        quick_sort(arr, left, new_pivot-1)
        quick_sort(arr, new_pivot+1, right)

@timeit
def call(arr):
    quick_sort(arr, 0, len(arr)-1)

if __name__=='__main__':
    arr = [5,21,4,6,12,33,15]

    base.print_arr(arr)
    call(arr)
    base.print_arr(arr)
