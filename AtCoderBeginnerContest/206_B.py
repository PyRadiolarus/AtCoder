# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
for i in range(1, N+1):
    if int(i * (i + 1) / 2) >= N:
        break
    else:
        pass
print(i)