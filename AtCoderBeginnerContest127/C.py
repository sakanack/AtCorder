N, M = map(int, input().split())

L = []
R = []
for _ in range(M):
    l,r = map(int, input().split())
    L.append(l)
    R.append(r)

masterkey = min(R) - max(L) + 1
if masterkey <= 0:
    print(0)
if masterkey > 0:
    print(masterkey)
