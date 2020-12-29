N, M = map(int, input().split())

a = [int(input()) for _ in range(M)]

for i in range(N-1):
    if a[i+1] - a[i] <= 1:
        print(0)
        exit()

