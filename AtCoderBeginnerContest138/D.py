N,Q = map(int,input().split())

edge = [tuple(map(int, input().split())) for _ in range(N-1)]
ope = [tuple(map(int, input().split())) for _ in range(Q)]

pointer = [[] for i in range(N+1)]
ans = [0] * (N+1)

print(edge)
print(ope)

for a,b in edge:
    pointer[a].append(b)

print(pointer)

for p,x in ope:
    ans[p] += x
    