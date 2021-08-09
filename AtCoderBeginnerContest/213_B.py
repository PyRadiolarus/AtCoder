from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
A = [int(i) for i in stdin.readline().split()]
A_ = sorted(A)
print(A.index(A_[-2])+1)