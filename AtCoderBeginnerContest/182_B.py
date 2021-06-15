# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

N = int(stdin.readline())
A = [int(i) for i in stdin.readline().split()]

deg_gcd = -1
res = 0

for i in range(2, 1001):
    k = sum(a % i == 0 for a in A)
    if res < k:
        res = k
        deg_gcd = i

print(deg_gcd)