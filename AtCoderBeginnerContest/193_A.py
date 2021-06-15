# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")
a, b = map(int, stdin.readline().rstrip().split())
ans = (a - b) / a * 100

print(ans)