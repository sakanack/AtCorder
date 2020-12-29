N = int(input())
P = list(map(int, input().split()))

min_dp = [-1] * N

min_dp[0] = P[0]

ans = 1
for i in range(1, N):
    if(P[i] <= min_dp[i-1]):
        min_dp[i] = P[i]
        ans += 1
    else:
        min_dp[i] = min_dp[i-1]

print(ans)