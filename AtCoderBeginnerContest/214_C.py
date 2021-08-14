#WA解
from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
S = [int(i) for i in stdin.readline().split()]
T = [int(i) for i in stdin.readline().split()]

for i in range(N):
    if i == 0:
        if T[0] <= S[0]:
            print(T[0])
        else:
            print(S[0])
    elif i == 1:
        sum_ = S[i-1] + T[i-1]
        if sum_ <= T[i]:
            print(sum_)
        else:
            print(T[i])
    else:
        latest = S[i-1] + T[i-1]
        sum_ += S[i-1]
        if latest <= sum_ and latest <= T[i]:
            print(latest)
        elif sum_ <= T[i]:
            print(sum_)
        else:
            print(T[i])