N,M = map(int, input().split())

shop = [tuple(map(int, input().split())) for _ in range(N)]

shop.sort()

count = 0
money = 0
for i in range(N):
    if count == M:
        break
    elif count + shop[i][1] <= M:
        count += shop[i][1]
        money += shop[i][0] * shop[i][1]
    elif count + shop[i][1] > M:
        money += shop[i][0] * (M - count)
        count += M - count

print(money)