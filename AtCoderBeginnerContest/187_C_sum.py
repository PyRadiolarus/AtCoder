# -*- coding: utf-8 -*-
# Python 3.8.2 で 2207ms/55704KB。TLE。
# PyPy3 7.3.0 で 2211ms/203000KB。TLE。
from sys import stdin
stdin = open("../../stdin.txt")

import itertools
N = int(stdin.readline().rstrip())
S = [stdin.readline().split() for i in range(N)]
S = set(sum(S,[]))

for c in S:
    if "!" + c in S:
        print(c)
        exit()
print("satisfiable")