# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

from collections import deque
N = int(stdin.readline().rstrip())
A = [-1] + [int(x) for x in stdin.readline().split()]

surviver = deque(range(1, 2 ** N + 1))

for i in range(N -1):
    winner = deque()
    while surviver:
        first = surviver.popleft()
        second = surviver.popleft()
        if A[first] > A[second]:
            winner.append(first)
        else:
            winner.append(second)
    surviver = winner

first = surviver.popleft()
second = surviver.popleft()

if A[first] > A[second]:
    print(second)
else:
    print(first)