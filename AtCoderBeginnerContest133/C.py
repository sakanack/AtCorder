L, R = map(int,input().split())

x = 2019
xL = L // x
xR = R // x
if xL < xR or L == 0:
    print(0)
    exit()

mL = L % x
mR = R % x

ans = 2019
for i in range(mL,mR):
    for j in range(i+1,mR+1):
        cr = (i*j)%2019
        if ans > cr:
            ans = cr
print(ans)
