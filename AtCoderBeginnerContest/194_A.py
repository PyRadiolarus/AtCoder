# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")
nonfat_ms, mfat = map(int, stdin.readline().split())
ms = nonfat_ms + mfat

if ms >= 15 and mfat >= 8:
    output = 1
elif ms >= 10 and mfat >= 3:
    output = 2
elif ms >= 3:
    output = 3
else:
    output = 4

print(output)