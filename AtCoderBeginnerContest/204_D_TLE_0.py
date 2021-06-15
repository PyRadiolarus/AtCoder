# 最初の提出コード
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

import itertools
N = int(stdin.readline())
T = tuple(int(i) for i in stdin.readline().split())
s_T = sum(T)
res = s_T
for oven in itertools.combinations(T,(N // 2)):
    oven_ = sum(oven)
    sub_oven = s_T - oven_
    if oven_ <= sub_oven:
        time = sub_oven
    else:
        time = oven_
    if res <= time:
        pass
    else:
        res = time
print(res)