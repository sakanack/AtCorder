import math

N = int(input())

X = math.floor(N / 1.08)

for i in range(2):
    ans = X+i
    if (math.floor(ans * 1.08) == N):
        print(ans)
        exit()
print(':(')