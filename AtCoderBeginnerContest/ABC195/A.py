# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")
M, H = map(int, stdin.readline().rstrip().split())

if H % M == 0:
    print("Yes")
else:
    print("No")