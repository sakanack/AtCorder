import math
N = int(input())
ABCDE = [int(input()) for _ in range(5)]

time = 4
print(time + math.ceil(N/min(ABCDE)))
