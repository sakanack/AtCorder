N = int(input())

def f(n):
    if(n < 2):
        return 1
    return n * f(n-2)

def zeroCount(numStr):
    count = 0
    for s in reversed(numStr):
        if(s != "0"):
            return count
        count += 1

print(zeroCount(str(f(N))))

print(f(N))