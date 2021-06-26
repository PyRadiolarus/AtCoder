from sys import stdin
stdin = open("../stdin.txt")

A, B, C, D = map(int, stdin.readline().split())
bb = A
rb, res = 0, 0
if (B / C > D) or (D == 1 and B == C and A != 1):
    res = -1
elif A <= D:
    pass
else:
    for i in range(1,10**5+1):
        bb += B
        rb += C
#        l = B * i + A
#        r = D * C * i
        res += 1
        if bb > D * rb:
            pass
        else:
            break
print(res)