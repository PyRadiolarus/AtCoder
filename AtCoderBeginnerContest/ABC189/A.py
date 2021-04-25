# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

C = stdin.readline()

if C[0] == C[1] == C[2]:
    print("Won")
else:
    print("Lost")