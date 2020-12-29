N, M = map(int,input().split())
A = list(map(int, input().split()))

BC = [list(map(int, input().split())) for _ in range(M)]

A.sort()
BC.sort(reverse = True, key=lambda x : x[1])

index = -1
for b, c in BC:
    for _ in range(b):
        index += 1
        if index >= N:
            break
        if A[index] >= c:
            break
        A[index] = c
    else:
        continue
    break
print(sum(A))
