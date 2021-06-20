# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
A = [int(i) for i in stdin.readline().split()]
res = 0
if N == len(set(A)):
    res = int((N * (N - 1)) / 2)
else:
    for i in range(1,N+1):
        for j in range(i, N+1):
            if A[i-1] == A[j-1]:
                pass
            else:
                res += 1
print(res)