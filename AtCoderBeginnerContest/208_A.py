from sys import stdin
stdin = open("../stdin.txt")

A, B = map(int, stdin.readline().split())
if B / 6 <= A and A <= B:
    print("Yes")
else:
    print("No")