# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N = int(stdin.readline())
res = N
for i in range(1,N+1):
    if ("7" in str(i)) or ("7" in oct(i)):
        res -= 1
print(res)