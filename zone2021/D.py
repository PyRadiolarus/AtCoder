# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

import re

def validate(text):
    return not re.search(r"(.)\1{2,}", text)

S = stdin.readline().rstrip()
N = len(S)
T = ""

for i in range(N+1):
    if S[i] == "R":
        T = T[::-1]
    else:
        T = T + S[i]
    

print(type(S))