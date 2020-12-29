N = int(input())
A = list(map(int, input().split()))

order = list(zip(range(1,N+1), A))
order = sorted(order, key=lambda x: x[1])

for o in order:
    print(o[0], end=" ")
print("")