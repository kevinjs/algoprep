#!/usr/bin/env python
import math
import base
from base import timeit

def get_parent(idx):
    return int(math.floor(idx/2))

def get_left_child(idx):
    return idx * 2 + 1

def get_right_child(idx):
    return idx * 2 + 2

def init_heap(arr):
    half = int(math.floor(len(arr)/2)) - 1
    for i in xrange(half, -1, -1):
        modify_heap(arr, i)
    return arr

def modify_heap(arr, idx_root):
    l_c = get_left_child(idx_root)
    r_c = get_right_child(idx_root)

    if l_c < len(arr):
        if arr[idx_root] > arr[l_c]:
            base.swap(arr, idx_root, l_c)
        if get_left_child(l_c) or get_right_child(l_c):
            modify_heap(arr, l_c)
    if r_c < len(arr):
        if arr[idx_root] > arr[r_c]:
            base.swap(arr, idx_root, r_c)
        if get_left_child(r_c) or get_right_child(r_c):
            modify_heap(arr, r_c)

@timeit
def heap_sort(arr):
    # heap sort
    # modify recursively
    # move 1st element to last and modify [0:len-i-1]
    for i in xrange(0, len(arr)):
        arr[0:len(arr)-i] = init_heap(arr[0:len(arr)-i])
        base.swap(arr, 0, len(arr)-i-1)


if __name__=='__main__':
    arr = [5, 21, 4, 6, 12, 33, 15, 195, 27, 31, 57]

    base.print_arr(arr)
    heap_sort(arr)
    base.print_arr(arr)
