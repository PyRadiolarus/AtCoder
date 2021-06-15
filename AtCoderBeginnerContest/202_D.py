# -*- coding: utf-8 -*-
# Python 3.8.2 で 2230ms/691928KB。TLE。
# PyPy3 7.3.0 で 2223ms/533456KB。TLE。
from sys import stdin
stdin = open("../../stdin.txt")

import itertools
A, B, K = map(int, stdin.readline().split())
s = "a" * A + "b" * B
anaglam_list = ["".join(i) for i in itertools.permutations(s)]
res = sorted(list(set(anaglam_list)))
print(res[K-1])