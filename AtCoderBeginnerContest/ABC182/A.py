# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

A, B = map(int, stdin.readline().split())

print(((2*A + 100) - B))