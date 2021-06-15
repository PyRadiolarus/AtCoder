# Python 3.8.2 で提出、2206 ms / 18268 KB でTLE。コード長 144 byte。
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

A, B, C = map(int, stdin.readline().split())
ac = A ** C
bc = B ** C
if ac < bc:
    print("<")
elif ac > bc:
    print(">")
else:
    print("=")