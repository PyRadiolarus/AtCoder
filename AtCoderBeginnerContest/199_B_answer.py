# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

N = int(stdin.readline().rstrip())
ListA = list(map(int, stdin.readline().split()))
ListB = list(map(int, stdin.readline().split()))

count = 0
for i in range(1,1001):
    ok = True
    for j in range(N):
        if i < ListA[j] or i > ListB[j]:
            ok = False
    if ok:
        count += 1
print(count)