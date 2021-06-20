# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

import itertools
N = int(stdin.readline())
A = [int(i) for i in stdin.readline().split()]
res = 0
t = itertools.combinations(A,2)
for x in t:
    a, b = x
    if a == b:
        pass
    else:
        res += 1
print(res)
