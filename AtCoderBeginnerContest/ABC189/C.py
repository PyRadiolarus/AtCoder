# Pythonで提出すると、実行時間制限1.5secに対し、1.6sec台が頻発してTLEになる。メモリ使用量は10MB程度。
# PyPyなら実行時間は0.3sec程度でACを出せる。メモリ使用量は69MB程度。メモリ使用量はPythonと比べて約7倍だが、メモリ制限は1GBなので全く気にならない。
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N = int(stdin.readline().rstrip())
A = [*map(int, stdin.readline().rstrip().split())]

ans = 0
for l in range(N):
    m = 10 ** 5 + 1
    for r in range(l, N):
        d = r - l + 1
        m = min(m, A[r])
        score = m * d
        ans = max(ans, score)
print(ans)