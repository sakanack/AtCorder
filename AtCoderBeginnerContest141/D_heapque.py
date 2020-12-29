import heapq as hq
import math

N,M = map(int,input().split())
A = list(map(lambda x: int(x)* -1,input().split()))
hq.heapify(A)

for _ in range(M):
    a = math.ceil(hq.heappop(A) / 2)
    hq.heappush(A,a)

print(sum(A)* -1)