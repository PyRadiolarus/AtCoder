# -*- coding: utf-8 -*-
# Python 3.8.2 で 427ms/64780KB。AC。
# PyPy3 7.3.0 で 392ms/122272KB。AC。
from sys import stdin
stdin = open("stdin.txt")

import itertools
N = int(stdin.readline().rstrip())
S = [stdin.readline().split() for i in range(N)]
S = set(itertools.chain.from_iterable(S))

for c in S:
    if "!" + c in S:
        print(c)
        exit()
print("satisfiable")