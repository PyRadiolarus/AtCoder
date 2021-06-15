# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

import copy
S = list(str(stdin.readline().rstrip()))
new_S = S[::-1]
res = []
for i in range(len(S)):
    s = new_S[i]
    if s == "6":
        s = str(9)
    elif s == "9":
        s = str(6)
    else:
        pass
    res.append(s)
out = "".join(res)
print(out)