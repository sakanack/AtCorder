import math
import time

N,M = map(int,input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
A.append(-1)
A.insert(0,-1)
print(A)

def discount(price):
    return math.floor(price / 2)

p = 1
while(M != 0):
    print("p,a",p,A[p])
    print(A)
    if A[p] <= A[p-1]:
        if A[p-1] <= A[p+1]:
            p= p+1
        else:
            p = p-1
        continue
    if A[p] <= A[p+1]:
        p = p+1
        continue
    
    A[p] = discount(A[p])
    print(A[p])
    M -= 1
    print("M:",M)

print(A)
print(sum(A)+2)
