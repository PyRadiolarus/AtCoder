# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().split()]

res = 0

for i in range(N):
    for j in range(N):
        if i >= j:
            pass
        else:
            a = A[i]
            b = A[j]
            if (a - b) % 200 == 0:
                res += 1
            else:
                pass
print(res)