import math

a,b,x = map(int,input().split())

h = b - (x / (a*a) )

print(b,a)
print(math.degrees(math.atan2(b,a)))