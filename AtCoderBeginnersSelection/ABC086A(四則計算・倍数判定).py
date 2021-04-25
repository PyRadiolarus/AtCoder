##########################
### -*- 問題 -*- ##########
#【問題概要】
# 二つの正整数 a, b が与えられます。 a と b の積が偶数か奇数か判定してください。

#【制約】
# 1 ≤ a,b ≤ 10000
# a, b は整数

#【数値例】
# (1)
#　a=3
#　b=4
#　答え: Even

# 3 × 4 = 12 でこれは偶数なので、"Even" を出力します。

# (2)
#　a=1
#　b=21
#　答え: Odd

# 1 × 21 = 21 でこれは奇数なので、"Odd" を出力します。

#【標準入力形式】
# a b
##########################
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")
# 整数の入力
a, b = map(int, stdin.readline().split())
#a, b = map(int, input().split())
x = a * b
if x % 2 == 0:
    print("Even")
else:
    print("Odd")