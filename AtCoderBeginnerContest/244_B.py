# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")
N = int(stdin.readline())
T = stdin.readline()
x = 0
y = 0
mode_ = "E"
for i in T:
    if i == "S":
        if mode_ == "E":
            x += 1
        elif mode_ == "S":
            y -= 1
        elif mode_ == "W":
            x -= 1
        else:
            y += 1
    else:
        if mode_ == "E":
            mode_ = "S"
        elif mode_ == "S":
            mode_ = "W"
        elif mode_ == "W":
            mode_ = "N"
        else:
            mode_ = "E"
print(x,y)