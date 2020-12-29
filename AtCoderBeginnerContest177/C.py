N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        # print("i,j=",i,j)
        # print(A[i], A[j])
        ans += A[i] * A[j]
print(ans % (10**9+7))