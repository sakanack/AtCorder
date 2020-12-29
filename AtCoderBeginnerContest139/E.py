N = int(input())
A = [list(map(int,(input().split()))) for _ in range(N)]

day = 0
vs_list = {}
for i in range(N):
    vs_list[i+1]=  A[i].pop(0)
    print(vs_list)

for i in range(1,N+1):
    if i == vs_list[vs_list[i]]:
        print(vs_list[vs_list[i]],vs_list[i])