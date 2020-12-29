N, M, C = map(int, input().split())
B = list(map(int, input().split()))

A = [ list(map(int, input().split())) for _ in range(N) ]

count = 0
for i in range(N):
    if sum([x*y for x,y in zip(A[i], B)]) + C > 0:
        count += 1

print(count)