# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N, S, D = map(int, stdin.readline().rstrip().split())
res = ("No")
for _ in range(N):
    s, d = map(int, stdin.readline().rstrip().split())
    if s < S and D < d:
        res = ("Yes")
    else:
        pass
print(res)
