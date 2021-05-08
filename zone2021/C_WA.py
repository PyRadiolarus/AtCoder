# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

import itertools
N = int(stdin.readline().rstrip())
l = [stdin.readline().split() for i in range(N)]
l = list(itertools.chain.from_iterable(l))
l_i = [int(i) for i in l]

power = l_i[0::5]
speed = l_i[1::5]
technique = l_i[2::5]
knowledge = l_i[3::5]
imagination = l_i[4::5]

t_p = max(power)
t_s = max(speed)
t_t = max(technique)
t_k = max(knowledge)
t_i = max(imagination)

res = min(t_p, t_s, t_t, t_k, t_i)


print(res)