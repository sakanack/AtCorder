A,B,X = map(int, input().split())

def keta(num):
    return len(str(num))

N = 0
for n in range(10,-1,-1):
    seisu = 1 * (10**n)
    for i in range(9,0,-1):
        kijun = seisu * i
        if X < (A * (N + kijun) + B * keta(N + kijun)):
            continue
        else:
            N += kijun
            break

print(min(N,1000000000))