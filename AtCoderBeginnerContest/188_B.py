# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().split()]
B = [int(x) for x in stdin.readline().split()]
l = []
for i in range(N):
    res = A[i] * B[i]
    l.append(res)

res = sum(l)

if res != 0:
    print("No")
else:
    print("Yes")