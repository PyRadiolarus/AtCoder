# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

a, b, c = map(int, stdin.readline().split())
s = 7
res = (s-a) + (s-b) + (s-c)
print(res)