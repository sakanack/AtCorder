N = int(input())
W = list(map(int, input().split()))

ans = sum(W)
for i in range(N+1):
    sa = abs(sum(W[:i]) - sum(W[i:N+1:]))
    if ans > sa:
        ans = sa
print(ans)