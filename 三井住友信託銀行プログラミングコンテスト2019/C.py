X = int(input())

X1 = X % 100

counter = 0
minusV = 5
while(X1 != 0):
    if(X1 - minusV >= 0):
        X1 = X1 - minusV
        counter += 1
    else:
        minusV -= 1

if(counter*100 <= X):
    print('1')
else:
    print('0')