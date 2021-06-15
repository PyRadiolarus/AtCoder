# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N, W = map(int, stdin.readline().split())
res = N // W

print(res)