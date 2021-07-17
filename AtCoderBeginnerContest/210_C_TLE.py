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
