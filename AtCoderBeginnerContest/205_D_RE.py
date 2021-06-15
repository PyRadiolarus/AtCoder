# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

import sys
sys.setrecursionlimit(10000000)
N, Q = map(int, stdin.readline().split())
A = set([int(i) for i in stdin.readline().split()])
K = [int(stdin.readline()) for i in range(Q)]
l = set([int(i) for i in range(1, 10 * len(K) + 1)]) - A
l = list(l)
for i in range(Q):
    j = K[i]
    print(l[j-1])