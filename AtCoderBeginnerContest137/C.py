N = int(input())
S = [input() for _ in range(N)]

dic = {}
ans = 0
for s in S:
    sortstr = str(sorted(s))
    if sortstr in dic:
        ans += dic[sortstr]
        dic[sortstr] += 1
    else:
        dic[sortstr] = 1
print(ans)