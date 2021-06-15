# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

X, Y = map(int, stdin.readline().split())
lower = min(X, Y) + 3
if lower > max(X, Y):
    print("Yes")
else:
    print("No")