import math

A, B = map(int,input().split())

def lcm(a,b):
    return int(a * b / math.gcd(a,b))

print(lcm(A,B))