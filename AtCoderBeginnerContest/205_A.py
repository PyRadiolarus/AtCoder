# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

A, B = map(int, stdin.readline().split())
print(A * B / 100)