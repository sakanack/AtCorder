N = int(input())

S = []
P = []
for i in range(N):
    sp = input().split()
    S.append(sp[0])
    P.append(int(sp[1]))

SP = list(zip(range(1,N+1),S,P))

SP.sort(reverse = True, key = lambda x : x[2])
SP.sort(key = lambda x : x[1])

for i in SP:
    print(i[0])