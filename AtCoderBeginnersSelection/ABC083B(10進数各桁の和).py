##########################
### -*- 問題 -*- ##########
#【問題概要】
# 1 以上 N 以下の整数のうち、10 進法で各桁の和が A 以上 B 以下であるものについて、総和を求めてください。

#【制約】
# 1 ≤ N ≤ 10^4
# 1 ≤ A ≤ B ≤ 36
# 入力はすべて整数

#【数値例】
# (1)
#　N=20
#　A=2
#　B=5
#　答え: 84
# 20 以下の整数のうち、各桁の和が 2 以上 5 以下なのは、2, 3, 4, 5, 11, 12, 13, 14, 20 です。これらの合計である 84 を出力します。

#【標準入力形式】
# N A B

##########################
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")
n, a, b = map(int,stdin.readline().split())
l = list(range(1,n+1))
num = []
res = 0

for i in range(n):
    s = sum(list(map(int, str(l[i]))))
    if a <= s <= b:
        res += l[i]
print(res)