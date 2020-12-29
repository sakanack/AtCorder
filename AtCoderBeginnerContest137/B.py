K,X = map(int,input().split())

left = X - (K-1)
if left < -1000000:
    left = -1000000

right = X + (K-1)
if right > 1000000:
    right = 1000000

for i in range(left,right+1):
    print(i,end=" ")

print("")