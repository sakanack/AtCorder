from fractions import gcd

A,B,C,D = map(int, input().split())

lcm = (C*D) // gcd(C,D)

b_sum = B - ((B//C) + (B//D) - (B//lcm))

a = A-1
a_sum = a - ((a//C) + (a//D) - (a//lcm))

print(b_sum - a_sum)