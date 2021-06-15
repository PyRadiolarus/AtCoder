# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

A, B = stdin.readline().split()

S_A = int(A[0]) + int(A[1]) + int(A[2])
S_B = int(B[0]) + int(B[1]) + int(B[2])

if S_A == S_B:
    print(S_A)
else:
    print(max(S_A, S_B))