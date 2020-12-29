import numpy as np

N,D = map(int,input().split())

X_list = [np.array(list((map(int, input().split())))) for _ in range(N)]

ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        euc = np.linalg.norm(X_list[i] - X_list[j])
        if euc.is_integer():
            ans += 1

print(ans)
