# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N, X = map(int, stdin.readline().split())
s = 0
res = -1
for i in range(1, N+1):
    V, P = map(int, stdin.readline().split())
    s += V * P
    if s > 100 * X:
        res = i
        break
print(res)
