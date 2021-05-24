# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

S_x, S_y, G_x, G_y = map(float, stdin.readline().split())
print((S_x * G_y + G_x * S_y) / (S_y + G_y))
