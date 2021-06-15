# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

H, W = map(int, stdin.readline().rstrip().split())
I = []

for _ in range(H):
    s = stdin.readline()
    I.append(s)

ans = 0

for row in range(H - 1):
    for col in range(W - 1):
        A = []
        A.append(I[row][col]) #LeftUpper
        A.append(I[row + 1][col]) #LeftLower
        A.append(I[row][col + 1]) #RightUpper
        A.append(I[row + 1][col + 1]) #RightLower

        if A.count("#") == 1 or A.count("#") == 3:
            ans += 1

print(ans)