N = int(input())
V = list(map(int,input().split(' ')))
C = list(map(int,input().split(' ')))

total = 0
for v,c in zip(V,C):
    if v >= c:
        total += v - c
print(total)