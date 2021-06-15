# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

N, X = map(int, stdin.readline().split())
S = list(map(str, stdin.readline().rstrip()))

res = X
for i in range(N):
    tf = S[i]
    if tf == "o":
        res += 1
    else:
        if res == 0:
            pass
        else:
            res -= 1
print(res)