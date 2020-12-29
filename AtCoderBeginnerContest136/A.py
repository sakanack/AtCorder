A,B,C = map(int, input().split())

capa = A - B
ans = C - capa

if ans > 0:
    print(ans)
elif ans <= 0:
    print(0)
