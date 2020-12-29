N, K = map(int,input().split())

count = 0

sunuke = list(range(1,N+1))

for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        try:
            sunuke.remove(a)
        except ValueError:
            continue
print(len(sunuke))