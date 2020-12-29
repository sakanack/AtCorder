N,K,Q = map(int,input().split())
A = [int(input()) for _ in range(Q)]

life = [K-Q] * N
for i in range(Q):
    life[A[i]-1] += 1

for l in life:
    if l > 0:
        print("Yes")
    else:
        print("No")