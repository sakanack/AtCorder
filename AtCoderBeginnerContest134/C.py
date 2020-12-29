N = int(input())

A = [int(input()) for _ in range(N)]

sort_A = sorted(A, reverse=True)

for i in range(N):
    if A[i] == sort_A[0]:
        print(sort_A[1])
    else:
        print(sort_A[0])