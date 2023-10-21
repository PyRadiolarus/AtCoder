#TLE
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")
import math
L,R = map(int,stdin.readline().split())
x,y = L,R
a = 0
if math.gcd(x,y) == 1:
    a = y-x
else:
    for i in range((R-L)//2+1):
        for j in range((R-L)//2):
            if math.gcd((x+i),(y-j)) == 1:
                a = max(a,(y-j)-(x+i))
print(a)