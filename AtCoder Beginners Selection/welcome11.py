N = int(input())
txy = [tuple(map(int,input().split(' '))) for i in range(N)]

for t,x,y in txy:
    if (x + y) > t or (x + y - t) %2 != 0:
        print('No')
        exit()
print('Yes')