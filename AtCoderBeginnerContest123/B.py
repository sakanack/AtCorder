import math

order = [int(input()) for _ in range(5)]

def minus(x):
    return 0 if x == 0 else 10 - x

aaa = list(map(lambda x: math.ceil(x/10)*10, order))
bbb = list(map(lambda x: x%10,order))

print(sum(aaa) - max(map(minus,bbb)))
