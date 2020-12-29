H, N = map(int, input().split())

m = [list(map(int, input().split())) for _ in range(N)]

dpm = {}

for i in range(N):
    dpm[i] = m[i][0] / m[i][1]
    
print(dpm)

ans = 0
if (H // m[max(dpm, key=dpm.get)][0] >= 1):
    ans += (H // m[max(dpm, key=dpm.get)][0]) - 1
    H = (H % m[max(dpm, key=dpm.get)][0]) + m[max(dpm, key=dpm.get)][0]



print(ans, H)