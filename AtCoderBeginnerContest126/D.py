N = int(input())

side = [ list(map(int, input().split())) for _ in range(N-1)]
side.sort()

ans = [0] * (N+1)
for u, v, w in side:
    if w % 2 == 0:
        ans[v] = ans[u]
    if w % 2 == 1:
        ans[v] = (ans[u]+1) % 2

for a in ans[1:]:
    print(a)