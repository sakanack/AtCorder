import math
import itertools

X, Y = map(int, input().split())

moveTimes = (X+Y) / 3

if(not moveTimes.is_integer()):
    print(0)
    exit()

n = (2*Y - X) / 3
m = Y - 2*n
print(n,m)
if(n < 0):
    print(0)
    exit()
if(m < 0):
    print(0)
    exit()

