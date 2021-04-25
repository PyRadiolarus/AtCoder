##########################
### -*- 問題 -*- ##########
#【問題概要】
# 黒板に N 個の正の整数 A_1, …, A_N が書かれています。
# すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます。
# ・黒板に書かれている整数すべてを，2 で割ったものに置き換える。
# すぬけ君は最大で何回操作を行うことができるかを求めてください。

#【制約】
# 1 ≤ N ≤ 200
# 1 ≤ A_i ≤ 10^9

#【数値例】
# (1)
#　N=3
#　A=(16,12,24)
#　答え: 2
# 1 回操作を行うと (8, 6, 12) になります。2 回操作を行うと (4, 3, 6) になります。2 個目の 3 が奇数なため 3 回目の操作は行えません。

#【標準入力形式】
# N
# A_1 A_2 ... A_N
##########################
# -*- coding: utf-8 -*-
from sys import stdin
import copy
stdin = open("stdin.txt")
a = int(stdin.readline())
num = list(map(int, stdin.readline().split()))
res = 1
c = 0
l = []
for i in range(len(num)):
    if num[i] % 2 != 0:
        res = 0
        break
while res:
    lst=copy.deepcopy(num)
    num = []
    for n in range(0,a):
        b = lst[n] / 2
        if b % 2 != 0:
            res = 0
            break
        else:
            num.append(int(b))
    c += 1
print(c)
