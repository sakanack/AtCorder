N,Q = map(int,input().split(' '))
S = input()

lr = []
for _ in range(Q):
    lr.append(list(map(int,input().split(' '))))

index_list = []
start = 0
for i in range(N):
    if S[i-1] == 'A' and S[i] == 'C':
        start += 1
    index_list.append(start)

for l,r in lr:
    print(index_list[r-1] - index_list[l-1])