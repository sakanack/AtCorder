K = int(input())
A,B = map(int, input().split())

syou = A // K
mod = A % K

if mod == 0:
    print("OK")
    exit()
if (syou*K)+K <= B:
    print("OK")
else:
    print("NG")