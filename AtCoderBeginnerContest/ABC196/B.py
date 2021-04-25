# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")
import copy

X = stdin.readline().rstrip()
x_ = copy.copy(X)

f = "." in X

if f == True:
    a = X.find(".")
    x_ = x_[:a]
    x_ = int(x_)
else:
    x_ = int(x_)

print(x_)
