# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N = int(stdin.readline().rstrip())
out = N // 100

if N % 100 != 0:
    out += 1
else:
    pass

print(out)