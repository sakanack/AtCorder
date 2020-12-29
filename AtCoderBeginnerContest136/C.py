N = int(input())
H = list(map(int,input().split()))


for i in reversed(range(1,N)):
    ref = H[i] - H[i-1]
    if ref < -1:
        print("No")
        exit()
    elif ref == -1:
        H[i-1] -= 1

print("Yes")