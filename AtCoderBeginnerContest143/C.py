N = int(input())
S = input()

color = S[0]
ans = 1
for i in range(1,N):
    if color != S[i]:
        color = S[i]
        ans += 1

print(ans)