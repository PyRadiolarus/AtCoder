# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

A, B, C = map(int, stdin.readline().rstrip().split())
t = "Takahashi"
a = "Aoki"

if C == 0:
    if A > B:
        print(t)
    else:
        print(a)
else:
    if A >= B:
        print(t)
    else:
        print(a)