N = int(input())
A = list(map(int, input().split(' ')))

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

L = [0] * N
for i in range(N-1):
    L[i+1] = gcd(L[i],A[i])

R = [0] * N
for i in range(N-1,0,-1):
    R[i-1] = gcd(R[i],A[i])

ans = max([gcd(l,r) for l,r in zip(L,R)])
print(ans)