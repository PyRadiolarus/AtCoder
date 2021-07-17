from sys import stdin
stdin = open("../stdin.txt")

N, A, X, Y = map(int, stdin.readline().split())
diff = N - A
if N > A:
    print(X * A + Y * diff)
else:
    print(X * N)