from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
S = stdin.readline().rstrip()
c = S.index("1")
if c % 2 == 0:
    print("Takahashi")
else:
    print("Aoki")