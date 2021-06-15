# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")
N = int(stdin.readline())
data = [tuple(map(int, stdin.readline().split())) for _n in range(N)]
ans = float("inf")

for i in range(N):
    ai, bi = data[i]
    for j in range(N):
        aj, bj = data[j]
        time =  ai + bj if i == j else max(ai, bj)
        ans = min(ans, time)

print(ans)
