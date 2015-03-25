#!/usr/bin/env python

import base
from base import timeit

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    half = len(arr)/2
    sub_arr1 = [0 for i in range(0, half)]
    sub_arr1[:] = arr[0:half]
    sub_arr2 = [0 for i in range(0, len(arr) - half)]
    sub_arr2[:] = arr[half:]

    sub_arr1 = merge_sort(sub_arr1)
    sub_arr2 = merge_sort(sub_arr2)

    return merge_sub(sub_arr1, sub_arr2)

def merge_sub(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)

    comb_arr = [0 for i in range(0, len1+len2)]

    i=j=k=0

    while i<len1 and j <len2:
        if arr1[i] < arr2[j]:
            comb_arr[k] = arr1[i]
            i += 1
        else:
            comb_arr[k] = arr2[j]
            j += 1
        k += 1
    if i == len1:
        comb_arr[k:] = arr2[j:]
    else:
        comb_arr[k:] = arr1[i:]

    return comb_arr
    


@timeit
def call(arr):
    return merge_sort(arr)

if __name__=='__main__':
    arr = [5, 21, 4, 6, 12, 33, 5, 195, 27, 31, 57]

    base.print_arr(arr)
    arr = call(arr)
    base.print_arr(arr)
