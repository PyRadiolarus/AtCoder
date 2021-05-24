# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

x = int(stdin.readline().rstrip())

if x >= 0:
    print(x)
else:
    print(0)