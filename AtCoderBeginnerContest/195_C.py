# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

N = int(stdin.readline().rstrip())
if N >= 1000:
    v = N - 999
    if N >= 1000000:
        w = N - 999999
        if N >= 1000000000:
            x = N - 999999999
            if N >= 1000000000000:
                y = N - 999999999999
                if N >= 1000000000000000:
                    z = N - 999999999999999
                    print(v+w+x+y+z)
                else:
                    print(v+w+x+y)
            else:
                print(v+w+x)
        else:
            print(v+w)
    else:
        print(v)
else:
    print(0)

