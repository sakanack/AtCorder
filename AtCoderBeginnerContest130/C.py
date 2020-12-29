W,H,x,y = map(int, input().split())

area = (W * H) / 2

if (x * 2) == W and (y * 2) == H:
    another_ans = 1
else:
    another_ans = 0

print(area, another_ans)