# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N = int(stdin.readline().rstrip())
A = list(map(int, stdin.readline().rstrip().split()))

print(N)
print(A)
