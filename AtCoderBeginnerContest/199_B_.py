# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))

res = 0
for i in range(1, 1001) :
	ok = True
	for j in range(n):
		if i < a[j] or i > b[j] : ok = False
		if ok : res += 1
print(res)

