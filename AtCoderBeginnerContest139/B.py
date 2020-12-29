import math

A,B = map(int,input().split())

ans = 0
amount = 1
while(B > amount):
    amount += A - 1
    ans += 1
print(ans)