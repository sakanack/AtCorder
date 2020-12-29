N = int(input())
H = list(map(int,input().split()))

ans = 0
counter = 0
for i in range(N-1):
    if H[i] >= H[i+1]:
        counter += 1
    else:
        counter = 0

    if ans < counter:
        ans = counter

print(ans)