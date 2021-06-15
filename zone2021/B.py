# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

import math
import itertools

def getDistance(x1, y1, x2, y2):
    res = 0.0
    if y1 == y2:
        res = y1
    else:
        a = (y2 - y1) / (x2 - x1)
        b = y1 - (a * x1)
        res = b
    return res

N, D, H = map(int, stdin.readline().split())
l = [stdin.readline().split() for i in range(N)]
l = list(itertools.chain.from_iterable(l))
l_i = [int(i) for i in l]
x = l_i[0::2]
y = l_i[1::2]
out = 0.0

for i in range(N):
    out = max(getDistance(x[i], y[i], D, H), out)

print(out)
