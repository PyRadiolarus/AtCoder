# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

A, B, W = map(int, stdin.readline().split())
Wk = W * 1000
l = []

res = -1
for g in range(A,B+1):
    for h in range(g,B+1):
        for i in range(int(Wk/g)+1):
            for j in range(int(Wk/h)+1):
                if g * i + h * j == Wk:
                    k = i + j
                    l.append(k)
                    res += 1
if res == -1:
    print("UNSATISFIABLE")
else:
    print(min(l),max(l))