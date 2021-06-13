# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N = int(stdin.readline())
A = [int(i) for i in stdin.readline().split()]
l = [int(i) for i in range(1,N+1)]
A_s = sorted(A)

if A_s == l:
    print("Yes")
else:
    print("No")