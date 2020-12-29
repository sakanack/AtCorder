N, M = map(int,input().split())

A = list(map(int, input().split()))

A.sort(reverse=True)

amount = sum(A)

selectable = 0
for a in A:
    if(not (a*4*M < amount)):
        selectable += 1

if(selectable < M):
    print("No")
else:
    print("Yes")