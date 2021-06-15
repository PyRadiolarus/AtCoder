# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

N = int(stdin.readline())
A = [int(i) for i in stdin.readline().split()]
res = 0
for i in range(N):
    if A[i] <= 10:
        pass
    else:
        res += A[i] - 10
print(res)