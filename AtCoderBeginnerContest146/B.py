N = int(input())
S = input()

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for s in S:
    snum = alpha.index(s)
    henkango = (snum + N) % 26
    print(alpha[henkango],end='')

print('')