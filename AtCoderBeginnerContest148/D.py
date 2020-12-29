N = int(input())
a = list(map(int, input().split()))

breakCount = 0
orderCount = 1

for i in range(N):
    if(a[i] == orderCount):
        orderCount += 1
        continue
    breakCount += 1

if(breakCount == N):
    print(-1)
else:
    print(breakCount)