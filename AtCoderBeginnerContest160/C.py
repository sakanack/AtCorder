K, N = map(int, input().split())

A = list(map(int, input().split()))

dist = A[0] + (K-A[N-1])

for i in range(N-1):
    if (dist < A[i+1]-A[i]):
        dist = A[i+1]-A[i]

print(K - dist)
