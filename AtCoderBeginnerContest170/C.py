X, N = map(int, input().split())
p = list(map(int, input().split()))

antip = set(range(-110,210)) - set(p)
dist = 1000
ans = 1000
for v in antip:
    can = abs(v - X)
    if(can < dist):
        dist = can
        ans = v
    if(can == dist):
        ans = min(ans, v)
print(ans)