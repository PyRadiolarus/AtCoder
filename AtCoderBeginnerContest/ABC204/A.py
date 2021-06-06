# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

x, y = map(int,stdin.readline().split())
if x == y:
    print(x)
else:
    print(3 - (x + y))