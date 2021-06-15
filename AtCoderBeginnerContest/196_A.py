# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

a, b = map(int, stdin.readline().rstrip().split())
c, d = map(int, stdin.readline().rstrip().split())

ab = list(range(a, b+1))
cd = list(range(c, d+1))

print(max(ab)-min(cd))