# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")
import copy

N = int(stdin.readline().rstrip())
ListA = list(map(int, stdin.readline().split()))
ListB = list(map(int, stdin.readline().split()))

for i in range(N):
    l_i = list(range(ListA[i],ListB[i]+1))
    s_i = set(l_i)
    if i == 0:
        l_old = copy.deepcopy(l_i)
    else:
        pass
    s_old = set(l_old)
    out = s_i & s_old
    #l_old = copy.deepcopy(l_i)
    if len(s_i) == 1:
        out = 0
        
if out == 0:
    count = 0
else:
    count = len(out)

print(count)