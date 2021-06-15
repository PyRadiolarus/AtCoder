# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

a, b, c = map(int, stdin.readline().split())

if a == b:
    print(c)
elif a == c:
    print(b)
elif b == c:
    print(a)
else:
    print(0)