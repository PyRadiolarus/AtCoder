# Python 3.8.2 で 3380ms/2471688KB。TLE。
# PyPy3 7.3.0 で 3354ms/1459020KB。TLE。
from sys import stdin
stdin = open("../stdin.txt")

import itertools, math
from functools import reduce

def gcd_(*numbers):
    return reduce(math.gcd, numbers)

N = int(stdin.readline())
l = [list(stdin.readline().split()) for i in range(N)]
l = [[int(i) for i in j] for j in l]
#l_t = [list(v) for v in zip(*l)]
p = list(itertools.product(*l))
for i in range(len(p)):
    c = p[i]
    res = gcd_(*c)
    if res == 1:
        break
    else:
        pass
if res == 1:print("Yes")
else:print("No")