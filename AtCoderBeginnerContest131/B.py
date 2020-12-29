N, L = map(int, input().split())

taste = [L+i-1 for i in range(1,N+1)]
amount_taste = sum(taste)

if L < 0 and L+N-1 < 0:
    ans = amount_taste - max(taste)
elif L <= 0 and 0 <= L+N-1:
    ans = amount_taste
elif 0 < L and 0 < L+N-1:
    ans = amount_taste - min(taste)

print(ans)