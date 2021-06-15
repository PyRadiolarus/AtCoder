# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

import itertools
N, K = map(int, stdin.readline().split())
AB = [stdin.readline().split() for i in range(N)]
AB = sorted(AB)
AB = itertools.chain.from_iterable(AB)
AB_i = [int(i) for i in AB]
A = AB_i[0::2]
B = AB_i[1::2]

res = 0

for i in range(N):
    if i == 0:
        money = K
    else:
        money = money - (A[i]-A[i-1])
        if money < 0:
            res = A[i] + money + A[i-1]
            break
    if money < 0:
        res = A[i] + money + A[i-1]
        break
    else:
        if i == 0:
            money = money - A[i]
        else:
            money = money - (A[i]-A[i-1])
        if money < 0:
            res = A[i] - res
            break
        else:
            money = money + B[i]
            res = A[i]

if money >= 1:
    res += money
    print(res)
else:
    print(res)
