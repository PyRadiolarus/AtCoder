from sys import stdin
stdin = open("../stdin.txt")

A, B = map(int, stdin.readline().split())
if A >= B:
    print(0)
else:
    print(B - A + 1)