N = int(input())

keta = len(str(N))
ans = 0
for i in range(1,6,2):
    if keta > i:
        ans += 9 * (10**(i-1))
    if keta == i:
        ans += N - (10**(i-1)) + 1
print(ans)