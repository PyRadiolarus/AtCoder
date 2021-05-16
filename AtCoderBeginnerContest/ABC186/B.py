# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

import itertools
H, W = map(int, stdin.readline().split())
A = []
for i in range(H):
    A.append(list(map(int,stdin.readline().split())))
A_flatten = list(itertools.chain.from_iterable(A))
A_min = min(A_flatten)

res = 0
for j in range(len(A_flatten)):
    ans = A_flatten[j] - A_min
    res = res + ans

print(res)