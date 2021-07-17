# Python 3.8.2 で 2207ms/43760KB。TLE。
# PyPy3 7.3.0 で 2212ms/185536KB。TLE。
from sys import stdin
stdin = open("../stdin.txt")

N, K = map(int, stdin.readline().split())
C = [int(i) for i in stdin.readline().split()]
n = 0
if N == K:
    print(len(set(C)))
else:
    for i in range(N-K+1):
        s = set(C[i:i+K])
        a = len(s)
        if n>=a:pass
        else:n=a
    print(n)
