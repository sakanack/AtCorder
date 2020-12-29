import sys

a,b = input().split(' ')

def isOdd_Even(a, b):
    x = (int(a) * int(b)) % 2
    if(x == 1):
        print('Odd')
    else:
        print('Even')

isOdd_Even(a,b)