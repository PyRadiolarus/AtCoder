# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

N = int(stdin.readline().rstrip())
for i in range(1, 1000001):
    if int(str(i) * 2) > N:
        print(i - 1)
        exit()



