import queue
import itertools

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

searchQueue = queue.Queue()

def maxDist():
    while(not searchQueue.empty()):
        nowPos = searchQueue.get()
        h,w = nowPos
        up = (h-1, w)
        right = (h, w+1)
        down = (h+1, w)
        left = (h, w-1)
        nextPos(nowPos,up)
        nextPos(nowPos,right)
        nextPos(nowPos,down)
        nextPos(nowPos,left)
    return max(list(itertools.chain(*dist)))

def nextPos(nowPos, pos):
    h,w = pos
    if(h < 0 or h >= H):
        return
    if(w < 0 or w >= W):
        return
    if(S[h][w] == "#"):
        return
    if(dist[h][w] != -1):
        return
    searchQueue.put(pos)
    dist[h][w] = dist[nowPos[0]][nowPos[1]] + 1
    
ans = 0
for h in range(H):
    for w in range(W):
        dist = [[-1]* W for i in range(H)]
        if(S[h][w] == "#"):
            continue
        dist[h][w] = 0
        searchQueue.put((h,w))
        maxkouho = maxDist()
        if(ans < maxkouho):
            ans = maxkouho
print(ans)
        
