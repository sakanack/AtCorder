N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0
for i in range(N):
    if B[i] <= A[i]:
        ans += B[i]
        continue
    
    if B[i] > A[i]:
        r = B[i] - A[i]
        if r <= A[i+1]:
            ans += A[i] + r
            A[i+1] = A[i+1] - r
            continue
        
        if r > A[i+1]:
            ans += A[i] + A[i+1]
            A[i+1] = 0
            continue
print(ans)