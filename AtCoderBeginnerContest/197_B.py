# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

H, W, X, Y = map(int, stdin.readline().rstrip().split())
S = [stdin.readline().rstrip() for _ in range(H)]
out = 0

if H < X+1:
    I = H
else:
    I = X

if W < Y+1:
    J = W
else:
    J = Y

for i in range(I-1,I+1):
    for j in range(J+1):
        if S[i][j] == ".":
            out += 1
        else:
            pass

print(out)