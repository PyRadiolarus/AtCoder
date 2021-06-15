# -*- coding: utf-8 -*-
# Python 3.8.2 で 2206ms/24136KB。TLE。
# PyPy3 7.3.0 で 2208ms/84960KB。TLE。
from sys import stdin
stdin = open("../../stdin.txt")

N = int(stdin.readline())
num_list = [list(map(int, stdin.readline().split())) for i in range(N)]

res = 0
for i in range(N):
    s = sum(range(num_list[i][0],num_list[i][1]+1))
    res += s
print(res)