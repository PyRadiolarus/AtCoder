# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

X, Y, Z = map(int, stdin.readline().split())

if X == Z:
    out = Y-1

else:
    tanka_t = Y / X
    su = tanka_t * Z
    out = int(su)
    if out / Z >= tanka_t:
        out -= 1
if out < 0:
    out = 0

print(out)