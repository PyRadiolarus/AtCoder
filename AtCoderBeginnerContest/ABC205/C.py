# Python 3.8.2 で提出、28 ms / 9232 KB でAC。コード長 711 byte。
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

A, B, C = map(int, stdin.readline().split())
if 0 < A < B:
    print("<")
    exit()
elif 0 < B < A:
    print(">")
    exit()
elif A == B:
    print("=")
    exit()
else:
    pass

if C % 2 == 0:
    if (A <= 0 and B > 0) or (B <= 0 and A > 0):
        if abs(A) == abs(B):
            print("=")
        elif abs(A) < abs(B):
            print("<")
        else:
            print(">")
    else:
        if A < B:
            print(">")
        else:
            print("<")
    exit()

else:
    if A <= 0 and B > 0:
        print("<")
    elif B <= 0 and A > 0:
        print(">")
    else:
        if A < B:
            print("<")
        else:
            print(">")
    exit()