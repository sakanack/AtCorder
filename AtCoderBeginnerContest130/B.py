N, X = map(int,input().split())
L = list(map(int, input().split()))

count = 1
D = 0
for l in L:
    if D + l <= X:
        D = D + l
        count += 1
    else:
        break

print(count)
