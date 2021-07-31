from sys import stdin
stdin = open("../stdin.txt")

N, M = (int(i) for i in stdin.readline().split())
A = [int(i) for i in stdin.readline().split()]
B = [int(i) for i in stdin.readline().split()]
A, B = set(A), set(B)
out = 10**9 + 1
for i in A:
    for j in B:
        if abs(i-j) < out:out = abs(i-j)
        else:pass
print(out)