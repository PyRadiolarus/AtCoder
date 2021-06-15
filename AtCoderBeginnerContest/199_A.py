# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

A, B, C = map(int, stdin.readline().split())

if A*A + B*B < C*C:
    print("Yes")
else:
    print("No")