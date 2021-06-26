from sys import stdin
stdin = open("../stdin.txt")

A, B, C, D = map(int, stdin.readline().split())
bb = A
rb, res = 0, 0
if B / C > D:
    res = -1
elif D == 1 and B == C and A != 1:
    res = -1
elif A <= D:
    pass
else:
    while bb > rb * D:
        bb += B
        rb += C
        res += 1
        print(bb,rb,res)
        if bb <= rb * D:
            break
print(res)