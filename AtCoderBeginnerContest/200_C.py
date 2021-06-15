# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().split()]
A = [A[i] % 200 for i in range(N)]

res = 0
for i in set(A):
    x = A.count(i)
    res += x * (x-1) // 2

print(res)