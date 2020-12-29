N,M = map(int, input().split())

H = list(map(int, input().split()))

AB = [list(map(int, input().split())) for _ in range(M)]

print(AB)
count = 0
for i in range(1,N+1):
    for ab in AB:
        print(ab)
        if ab[0] == i-1:
            if H[i-1] <= H[ab[1]-1]:
                continue
        if ab[1] == i-1:
            if H[i-1] <= H[ab[0]-1]:
                continue
    count += 1
print(int(count/2))