N, K = map(int, input().split())

H = list(map(int, input().split()))
H.sort()

if(K >= N):
    print('0')
    exit()

print(sum(H[:N-K]))