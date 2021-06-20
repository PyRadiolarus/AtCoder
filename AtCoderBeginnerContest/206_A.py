# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline()) * 1.08
if int(N) < 206:
    print("Yay!")
elif int(N) == 206:
    print("so-so")
else:
    print(":(")