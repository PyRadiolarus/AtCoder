# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

import itertools
N = int(stdin.readline())
l = [stdin.readline().split() for i in range(N)]
l = list(itertools.chain.from_iterable(l))
l_i = [str(i) for i in l]
S = l_i[0::2]
T = l_i[1::2]
T = [int(s) for s in T]
T_sort = sorted(T, reverse=True)
meter = T.index(T_sort[1])
print(S[meter])