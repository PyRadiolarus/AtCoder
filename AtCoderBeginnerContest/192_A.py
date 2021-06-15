# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")
x = int(stdin.readline().rstrip())
y = int(x % 100)
res = 100 - y

print(res)