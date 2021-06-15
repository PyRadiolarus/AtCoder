# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

N, X = map(int, stdin.readline().rstrip().split())
A = list(map(int, stdin.readline().rstrip().split()))
A_ = str(-1)
A_ = [i for i in A if i != X]
A_ = [str(j) for j in A_]
A_ = " ".join(A_)

if A_ == -1:
    print("\n")
else:
    print(A_)