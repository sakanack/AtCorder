import numpy as np

N = int(input())
L = np.array(sorted(list(map(int, input().split())),reverse=True))

ans = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        min_range = abs(L[i] - L[j])
        max_range = L[i] + L[j]
        if max_range - min_range <= 1:
            break
        # print(L[j+1:])
        # print((min_range < L[j+1:]) & (L[j+1:] < max_range))
        ans += np.count_nonzero((min_range < L[j+1:]) & (L[j+1:] < max_range))
print(ans)