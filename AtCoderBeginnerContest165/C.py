import itertools
N,M,Q = map(int,input().split())

Sd = [list(map(int, input().split())) for i in range(Q)]
A = [1] * N

def point(ablock,A):
    p = 0
    for qlist in ablock:
        if(A[qlist[1]-1] - A[qlist[0]-1] == qlist[2]):
            p += qlist[3]
    return p

comb = itertools.combinations_with_replacement(range(1, M+1), N)

ans = 0
for c in comb:
    sug = point(Sd, c)
    if ans < sug:
        ans = sug

print(ans)