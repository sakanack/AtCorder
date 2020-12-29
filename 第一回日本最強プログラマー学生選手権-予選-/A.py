M,D = map(int, input().split())

ans = 0
for m in range(1,M+1):
    for d in range(1,D+1):
        d = str(d)
        if len(d) == 1:
            continue
        if int(d[0]) < 2:
            continue
        if int(d[1]) < 2:
            continue

        if int(d[0]) * int(d[1]) == m:
            ans += 1
print(ans)