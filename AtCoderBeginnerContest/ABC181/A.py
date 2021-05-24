# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N = int(stdin.readline())

if N % 2 == 0:
    print("White")
else:
    print("Black")