N = int(input())
A = list(map(int,input().split()))

minus = sum(x < 0 for x in A)

absA = list(map(abs,A))
if minus % 2 == 0:
    ans = sum(absA)
else:
    ans = sum(absA) - (2 * min(absA))

print(ans)