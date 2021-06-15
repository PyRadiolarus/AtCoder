##########################
### -*- 問題 -*- ##########
#【問題概要】
# 0 と 1 のみから成る 3 桁の番号 s_i が与えられます。1 が何個含まれるかを求めてください。

#【数値例】
# (1)
#　s = "101"
#　答え: 22
# '1' が 2 個含まれています。

#【標準入力形式】
# s_1s_2s_3
##########################
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")
n = stdin.readline()
num = list(map(int, n))
c = 0
for i in range (len(num)):
    if num[i] == 1:
        c = c + 1
    else:
        pass
print(c)