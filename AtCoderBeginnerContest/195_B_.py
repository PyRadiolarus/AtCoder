# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")
A, B, W = map(int, stdin.readline().split())
W *= 1000
m, M = 1 << 21, 0

for i in range(pow(10, 6) + 1):
    if A * i <= W <= B * i:
        m = min(m, i)
        M = max(M, i)
if M > 0:
    print(m, M)
else:
    print("UNSATISFIABLE")