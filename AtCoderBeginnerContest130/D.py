#しゃくとり法
N, K = map(int, input().split())

a = list(map(int, input().split()))

ans = 0
sum = 0
r = 0
for l in range(N):
    while(sum < K):
        if r == N:
            break
        sum += a[r]
        r += 1
    if (K <= sum):
        ans += N - r + 1
    sum -= a[l]

print(ans)