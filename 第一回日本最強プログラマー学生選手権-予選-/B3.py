N,K = map(int, input().split())
A = list(map(int,input().split()))
 
def souwa(num):
    if num % 2 == 0:
        return int((num+1) * (num/2))
    else:
        return int((num+1) * (num//2)) + ((num//2)+1)
 
ans = 0
for i in range(N):
    buf1 = sum(A[i] > A[j] for j in range(i+1, N))
    buf2 = sum(A[i] > a for a in A)
    ans += (buf1 * K) + (buf2 * (souwa(K-1)))
 
print(ans % (10**9+7))