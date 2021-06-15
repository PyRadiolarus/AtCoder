# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

A, B = map(int,stdin.readline().split())

A_1 = A // 100
A_2 = (A - A_1 * 100) // 10
A_3 = A - (100 * A_1 + 10 * A_2)
S_A = A_1 + A_2 + A_3

B_1 = B // 100
B_2 = (B - B_1 * 100) // 10
B_3 = B - (100 * B_1 + 10 * B_2)
S_B = B_1 + B_2 + B_3

if S_A == S_B:
    print(S_A)
else:
    print(max(S_A, S_B))