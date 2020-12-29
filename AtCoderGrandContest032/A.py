N = int(input())
b = list(map(int, input().split(' ')))

ans = []
while(b):
    position = -1
    for i,x in enumerate(b):
        order = i + 1
        if order == x:
            position = i
    if position == -1:
        print(-1)
        exit()
    ans.append(b.pop(position))

for a in ans[::-1]:
    print(a)