#!/usr/bin/env python

import random


def random_w(w):
    sum_w = sum(w)
    x = random.randint(0, sum_w-1)

    cnt = 0
    for i in range(len(w)):
	cnt += w[i]
        if cnt > x:
	    return i, x

if __name__=='__main__':
    w = [2, 1, 2, 3, 1, 1, 4]
    print 'weight:		', w
    dist = [0 for i in range(len(w))]

    for i in xrange(10000):
        idx, value = random_w(w)
	dist[idx] += 1

    print 'distribution:	', dist

