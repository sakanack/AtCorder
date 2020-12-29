import math

N, K = map(int, input().split())

pprob = 0
for n in range(1, N+1):
    if K/n < 1:
        throw = 0
    else:
        throw = math.ceil(math.log2(K/n))
    pprob += ((1 / 2) ** throw) / N

print(pprob)