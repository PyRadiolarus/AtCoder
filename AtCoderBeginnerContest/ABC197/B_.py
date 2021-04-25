# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

H, W, X, Y = map(int, stdin.readline().rstrip().split())
S = [stdin.readline().rstrip() for _ in range(H)]
out = 0

for i in X:
    for j in Y:
        if S[i][j] == ".":
            out += 1
        else:
            pass

print(out)