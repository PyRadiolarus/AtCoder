# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

An = list(map(int,stdin.readline().split()))
A_1 = An[0]
A_2 = An[1]
A_3 = An[2]

if A_3 - A_2 == A_2 - A_1:
    print("Yes")
else:
    out = sorted(An)
    A_1 = out[0]
    A_2 = out[1]
    A_3 = out[2]
    if A_3 - A_2 == A_2 - A_1:
        print("Yes")
    else:
        print("No")