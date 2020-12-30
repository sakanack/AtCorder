import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

conv = list(itertools.permutations(range(1,N+1), N))

pIndex = conv.index(P)
qIndex = conv.index(Q)

print(abs(pIndex - qIndex))