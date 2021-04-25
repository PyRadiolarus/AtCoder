# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")
N = int(stdin.readline())
inf = 1 << 30
ans = inf

for i in range(N):
    a, p, x = map(int, stdin.readline().rstrip().split())
    if x > a and ans > p:
        ans = p
if ans == inf:
    ans = -1

print(ans)
