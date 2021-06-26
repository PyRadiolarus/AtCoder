from sys import stdin
stdin = open("../stdin.txt")

n = [int(i) for i in stdin.readline().split()]
n.sort(reverse=True)
print(sum(n[:-1]))