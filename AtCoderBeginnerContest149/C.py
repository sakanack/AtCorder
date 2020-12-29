import math

X = int(input())

def isPrime(n):
    if(n < 0):
        return False
    if(n < 3):
        return True
    if(n % 2 == 0):
        return False
    for i in range(3, n, 2):
        if (n % i == 0):
            return False
    return True

def nextPrime(n):
    while(True):
        if isPrime(n):
            print(n)
            exit()
        n += 1

nextPrime(X)
        