import numpy as np

N = input()
A = input().split(' ')
NA = np.array(A, dtype='int64')

x = 0
while(True):
    if(np.all(NA % 2 == 0)):
        NA = NA / 2
        x = x + 1
    else:
        break
print(x)