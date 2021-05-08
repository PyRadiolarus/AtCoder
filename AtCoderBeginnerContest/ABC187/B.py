# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

import itertools
def getSloap(x1, y1, x2, y2):
    res = 0.0
    if y1 == y2:
        res = 0
    else:
        a = (y2 - y1) / (x2 - x1)
        b = y1 - (a * x1)
        res = a
    return res

N = int(stdin.readline().rstrip())
l = [stdin.readline().split() for i in range(N)]
l = list(itertools.chain.from_iterable(l))
l = [int(i) for i in l]
x = l[0::2]
y = l[1::2]

count = 0
for i in range(N):
    for j in range(i):
        if -1 <= getSloap(x[i], y[i], x[j], y[j]) <= 1:
            count += 1
print(count)
