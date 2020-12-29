N = int(input())
S = input()

kumi = [0] * N
for i in range(2,N):
    print(S[i:])
    kumi[i] = len(set(S[i:]))
    print('k',kumi[i])
print(kumi)

nset = set()
npos = list()
for i in range(N):
    if(S[i] not in nset):
        nset.add(S[i])
        npos.append(i)

print(nset)
print(npos)

ans = 0
for i in npos:
    if i > N-3:
        continue
    for j in range(i+1,N-1):
        nset = set()
        if(S[j] not in nset):
            nset.add(S[j])
            ans += kumi[j+1]
            print(ans,i,j)
print(ans)