N = int(input())
d = list(map(int, input().split()))
d.sort()

center = int(len(d) / 2)
print(d[center] - d[center-1])