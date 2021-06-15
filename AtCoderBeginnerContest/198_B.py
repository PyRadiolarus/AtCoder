# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

N = stdin.readline().rstrip()

if float(N) % 1 != 0:
    print("No")
    exit()

if N == N[::-1]:
    print("Yes")
    exit()

cp = round(len(N) / 2)
iout = 0

for i in range(cp,0,-1):
    if N[i] == str(0):
        iout += 1
    else:
        pass

N_zero = N.zfill(len(N) + iout)

if N_zero == N_zero[::-1]:
    print("Yes")
    exit()

cout = 0

for i in range(len(N)-1,0,-1):
    if N[i] == str(0):
        cout += 1
    else:
        break

N_z = N.zfill(len(N) + cout)

if N_z == N_z[::-1]:
    print("Yes")
    exit()

print("No")
