#全探索が思いつかず、コンテスト中は未提出
from sys import stdin
stdin = open("../stdin.txt")

S, T = (int(i) for i in stdin.readline().split())
res = 0
for i in range(S + 1):
    for j in range(S + 1 - i):
        for k in range(S + 1 - i - j):
            if i * j * k <= T:
                res += 1
print(res)