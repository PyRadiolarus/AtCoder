# -*- coding: utf-8 -*-
# Python 3.8.2 で 2206ms/28272KB。TLE。
# PyPy3 7.3.0 で 2209ms/103084KB。TLE。
from sys import stdin
stdin = open("stdin.txt")

N = int(stdin.readline())
A = [int(i) for i in stdin.readline().split()]
B = [int(i) for i in stdin.readline().split()]
C = [int(i) for i in stdin.readline().split()]

res = 0
for i in range(1,N+1):
    a = A[i-1]
    for j in range(1,N+1):
        c = C[j-1]
        if a == B[c-1]:
            res += 1
        else:
            pass
print(res)