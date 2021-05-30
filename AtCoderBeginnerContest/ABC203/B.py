# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N, K = map(int, stdin.readline().split())

res = 0

for i in range(1,N+1):
    for j in range(1,K+1):
        Num = i * 100 + j
        res += Num

print(res)