# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

A, B, C, D = map(int, stdin.readline().split())
print(min(A, B, C, D))