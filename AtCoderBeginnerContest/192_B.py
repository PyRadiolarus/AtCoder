# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")
S = stdin.readline().rstrip()

is_unreadable = all([c.islower() if i%2 == 0 else c.isupper() for i,c in enumerate(S)])

if is_unreadable:
    print("Yes")
else:
    print("No")