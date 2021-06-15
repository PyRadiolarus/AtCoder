# -*- coding: utf-8 -*-
from itertools import product
from sys import stdin
stdin = open("../../stdin.txt")

def bits():
    ans = 0
    for bit in product((0, 1), repeat=K):
        counter = [0] * (N + 1)
        for i in range(K):
            ball = pep[i][bit[i]]
            counter[ball] += 1

        score = 0
        for i in range(M):
            c, d = conditions[i]
            if counter[c] > 0 and counter[d] > 0:
                score += 1
        ans = max(ans, score)
    return ans


N, M = map(int, stdin.readline().rstrip().split())

conditions = []
for _ in range(M):
    a, b = map(int, stdin.readline().rstrip().split())
    conditions.append((a, b))

pep = []
K = int(stdin.readline().rstrip())
for _ in range(K):
    c, d = map(int, stdin.readline().rstrip().split())
    pep.append((c, d))

print(bits())
