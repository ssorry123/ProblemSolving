# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math
tmp = input().split()
N = (int)(tmp[0])
K = (int)(tmp[1])

input()

idx = 1
ret = 0
while idx <= N:
    if idx = 1:
        idx += K
        ret += 1
        continue
    idx += K-1
    ret += 1

print(ret)