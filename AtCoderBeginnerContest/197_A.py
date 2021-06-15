# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

S = list(stdin.readline().rstrip())
l = []
l.append(S[1])
l.append(S[2])
l.append(S[0])
ls = "".join(l)

print(ls)