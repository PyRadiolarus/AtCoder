# -*- coding: utf-8 -*-
from sys import stdin
from math import sqrt
stdin = open("../../stdin.txt")
N = int(stdin.readline().rstrip())
sr = int(sqrt(N))
s = set()

for a in range(2, sr + 1):
    x = a * a
    while x <= N:
        s.add(x)
        x *= a
print(N - len(s))