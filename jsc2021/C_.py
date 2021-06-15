# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")
import math

A, B = map(int, stdin.readline().split())
l = [1]

for i in range(A,B+1):
    for j in range(A,B+1):
        if i >= j:
            pass
        else:
            out = math.gcd(i,j)
            if l[0] >= out:
                pass
            else:
                l = [out]
print(l[0])