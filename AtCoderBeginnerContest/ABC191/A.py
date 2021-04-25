# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

V, T, S, D = map(int, stdin.readline().rstrip().split())

if T <= D / V <= S:
    print("No")
else:
    print("Yes")