from sys import stdin
stdin = open("../stdin.txt")

A, B = (int(i) for i in stdin.readline().split())
if 0 < A and B == 0:
    print("Gold")
elif A == 0 and 0 < B:
    print("Silver")
else:
    print("Alloy")