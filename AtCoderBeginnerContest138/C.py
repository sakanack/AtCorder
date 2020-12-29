N = int(input())
v = list(map(int,input().split()))

v.sort()

buf = v[0]
for i in range(1,N):
    buf =(buf + v[i]) / 2
print(buf)