# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

N, K = map(int, stdin.readline().split())

for i in range(K):
    if N % 200 != 0:
        N = str(N) + str(200)
    else:
        N = N / 200
    N = int(N)

print(N)