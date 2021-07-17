from sys import stdin
stdin = open("../stdin.txt")

N, X = map(int, stdin.readline().split())
A = [int(i) for i in stdin.readline().split()]
diff = len(A) // 2
if X >= sum(A) - diff:
    print("Yes")
else:
    print("No")