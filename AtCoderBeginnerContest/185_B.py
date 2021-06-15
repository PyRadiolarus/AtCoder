# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

import itertools
N, M, T = map(int, stdin.readline().split())
AB = [stdin.readline().split() for i in range(M)]
AB = itertools.chain.from_iterable(AB)
AB_i = [int(i) for i in AB]
A = AB_i[0::2]
B = AB_i[1::2]

for i in range(M):
    if i == 0:
        f = N - A[i]
    else:
        f = f - (A[i] - B[i-1])
    if f <= 0:
        break
    else:
        f = f + (B[i] - A[i])
        if f > N:
            f = N
        else:
            pass
final = f - (T - B[M-1])
if f <= 0 or final <= 0:
    print("No")
else:
    print("Yes")