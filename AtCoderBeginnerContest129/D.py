import numpy as np

H,W = map(int, input().split())

S = [list(input()) for _ in range(H)]

w_point = [[0 for i in range(W)] for j in range(W)]
for h in range(H):
    bw = 0
    for w in range(W):
        if S[h][w] == '#':
            for i in range(bw,w):
                w_point[h][i] = w - bw
            bw = w + 1
        if w == W -1:
            for i in range(bw, w+1):
                w_point[h][i] = w+1 - bw


h_point = [[0 for i in range(W)] for j in range(W)]
for w in range(W):
    bh = 0
    for h in range(H):
        if S[h][w] == '#':
            for i in range(bh,h):
                h_point[i][w] = h - bh
            bh = h + 1
        if h == H - 1:
            for i in range(bh, h+1):
                h_point[i][w] = h+1 - bh

print(np.max(np.array(w_point)+np.array(h_point)-1))