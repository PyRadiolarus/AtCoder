# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

from math import comb
L = int(stdin.readline())
X = L - 12
res = comb(X + 11, 11)
print(res)