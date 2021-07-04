from sys import stdin
stdin = open("../stdin.txt")

N, K = map(int, stdin.readline().split())
a = [int(i) for i in stdin.readline().split()]
a_ = sorted(a,reverse=True)
b, k = divmod(K, N)
k = k * -1
for i in a:
    if k == 0:
        print(b)
    elif i <= a_[k] and N != 1:
        print(b + 1)
    else:
        print(b)