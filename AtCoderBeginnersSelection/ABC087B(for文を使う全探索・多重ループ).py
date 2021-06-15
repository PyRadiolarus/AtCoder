##########################
### -*- 問題 -*- ##########
#【問題概要】
# 500 円玉を A 枚、100 円玉を B 枚、50 円玉を C 枚持っています。これらの硬貨の中から何枚かを選び、合計金額をちょうど X 円にする方法は何通りあるでしょうか？

#【制約】
# 0 ≤ A, B, C ≤ 50
# A + B + C ≥ 1
# 50 ≤ X ≤ 20000
# A, B, Cは整数である
# X は 50 の倍数である

#【数値例】
# (1)
#　A=2
#　B=2
#　C=2
#　X=100
#　答え:2
#条件を満たす選び方は以下の 2 通りです。
# 500 円玉を 0 枚、100 円玉を 1 枚、50 円玉を 0 枚選ぶ
# 500 円玉を 0 枚、100 円玉を 0 枚、50 円玉を 2 枚選ぶ

#【標準入力形式】
# A
# B
# C
# X
##########################
# -*- coding: utf-8 -*-
#a, b, c, x = int(stdin.readline()), int(stdin.readline()), int(stdin.readline()), int(stdin.readline())
a, b, c, x = map(int, open("../stdin.txt"))
s = 0
for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            if 500*i + 100*j + 50*k == x:
                s += 1

print(s)

#print(sum(500 * i + 100 * j + 50 * k == x for i in range(a+1)for j in range(b+1)for k in range(c+1)))