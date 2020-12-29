R, G, B, N = map(int, input().split())

box = sorted([R, G, B], reverse=True)

count = 0
for x in range(0, N+1, box[0]):
    for y in range(0, N+1 - x, box[1]):
        z = (N - x - y) / box[2]
        if z >= 0 and z.is_integer():
            count += 1
print(count)
