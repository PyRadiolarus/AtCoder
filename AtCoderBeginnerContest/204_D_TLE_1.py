# 試行錯誤コードその1
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

import itertools
N = int(stdin.readline())
T = tuple(int(i) for i in stdin.readline().split())
s_T = sum(T)
res = s_T
for oven in itertools.combinations(T,(N // 2)):
    oven_ = sum(oven)
    sub_oven = s_T - oven_
    if oven_ > sub_oven and oven_ < res:
        res = oven_
    elif oven_ <= sub_oven and sub_oven < res:
        res = sub_oven

print(res)