# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")
import math

A, B = map(int, stdin.readline().split())
list_x = list(range(A, B+1))
l = [1]

for i in range(len(list_x)):
    for j in range(1,len(list_x)):
        if i >= j:
            pass
        else:
            out = math.gcd(list_x[i],list_x[j])
            if l[0] >= out:
                pass
            else:
                l.clear()
                l.append(out)
print(l[0])