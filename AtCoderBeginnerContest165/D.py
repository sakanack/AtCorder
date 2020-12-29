import math
A,B,N = map(int,input().split())

def f (x,a,b):
    return math.floor(a*x/b) - a*(math.floor(x/b))

if( N < B):
    print(f(N,A,B))
else:
    print(f(B-1,A,B))