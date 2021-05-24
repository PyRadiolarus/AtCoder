# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

a, b = map(int, stdin.readline().split())
c, d = map(int, stdin.readline().split())

print((a*d - b*c))