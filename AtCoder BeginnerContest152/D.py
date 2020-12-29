N = int(input())

def ht(n):
    str_n = str(n)
    head = int(str_n[0])
    tail = int(str_n[-1])
    return (head, tail)

htmap = [[0] * 10 for i in range(10)]

for i in range(1, N+1):
    h,t = ht(i)
    htmap[h][t] += 1

ans = 0
for i in range(1, N+1):
    h,t = ht(i)
    ans += htmap[t][h]

print(ans)

