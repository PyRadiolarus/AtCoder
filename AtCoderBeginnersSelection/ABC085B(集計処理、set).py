##########################
### -*- 問題 -*- ##########
#【問題概要】
# N 個の整数 d_0, d_1, …, d_i が与えられます。
# この中に何種類の異なる値があるでしょうか？
# (原問題文をかなり意訳していますが、題意はこういうことです)

#【制約】
# 1 ≤ N ≤ 100
# 1 ≤ d_i ≤ 100
# 入力値はすべて整数
#【数値例】
# (1)
#　N=4
#　Q=3
#　d=(8,10,8,6)
#　答え:3
# 6, 8, 10 の 3 種類です。

#【標準入力形式】
# N
# d_1
# .
# .
# d_i
##########################
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")
N = int(stdin.readline())
num = []
for i in range(N):
    r = stdin.readline()
    num.append(r)
l = list(set(num))
print(len(l))
