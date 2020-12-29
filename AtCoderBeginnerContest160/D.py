N, X, Y = map(int, input().split())


count = [0] * (N-1)
for i in range(1, N+1):
    for j in range(i+1, N+1):
        routeA = abs(j-i)
        routeB = abs(X-i) + abs(Y-j) + 1
        min_route = min(routeA, routeB)
        count[min_route - 1] += 1

print('\n'.join(map(str, count)))