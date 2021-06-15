# 試行錯誤コードその2
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

import itertools
N = int(stdin.readline())
T = tuple(int(i) for i in stdin.readline().split())
s_T = sum(T)
res = s_T
for oven in itertools.combinations(T,(N // 2)):
    oven = sum(oven)
    res = min(max(oven,(s_T - oven)),res)

print(res)