# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N, M = map(int, stdin.readline().split())

A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))

s_A = set(A)
s_B = set(B)

s_R = s_A ^ s_B
out = list(s_R)

print(*out)