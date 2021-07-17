from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
C = list(map(int, stdin.readline().split()))
C.sort()
res = 1
for i in range(N):
    res = res * max(0, C[i] - i) % 1000000007
print(res)