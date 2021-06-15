# -*- coding: utf-8 -*-
# Python 3.8.2 で 206ms/9084KB。AC。
# PyPy3 7.3.0 で 172ms/69784KB。AC。
from sys import stdin
stdin = open("../../stdin.txt")

N = int(stdin.readline())
res = 0
for i in range(N):
    a, b = map(int, stdin.readline().split())
    res += b * (b + 1) // 2 - a * (a - 1) // 2
print(res)
