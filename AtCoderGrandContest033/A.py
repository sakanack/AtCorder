import numpy as np
import sys

H, W = map(int, input().split(' '))
A = np.array([list(input()) for i in range(H)])

b_pos = np.array(np.where(A == '#')).T
max_dist = 0
for h in range(H):
    for w in range(W):
        dist = np.amin(np.sum(np.abs(b_pos - (h, w)), axis=1))
        if dist > max_dist:
            max_dist = dist
print(max_dist)
