# -*- coding: utf-8 -*-
# デバッグ用は input() を stdin.readline() に置き換える。その際 コード最初の2行に以下を記載。
# from sys import stdin
# stdin = open("stdin.txt")

# デバッグ用コード
#from sys import stdin
#stdin = open("stdin.txt")
# 整数の入力
#a = int(stdin.readline())
# スペース区切りの整数の入力
#b,c = map(int,stdin.readline().split())
# 文字列の入力
#s = stdin.readline()
# 出力
#print("{} {}".format(a+b+c,s))

# 以下本番用
# 整数の入力
a = int(input())
# スペース区切りの整数の入力
b, c = map(int, input().split())
# 文字列の入力
s = input()
# 出力
print("{} {}".format(a+b+c, s))