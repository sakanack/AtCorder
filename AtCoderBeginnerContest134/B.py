import math

N,D = map(int, input().split())
ans = math.ceil(N / (2*D+1))
print(ans)