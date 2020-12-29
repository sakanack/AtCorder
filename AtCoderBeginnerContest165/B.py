X = int(input())

money = 100

counter = 0
while True:
    counter += 1
    money = money + int(money*0.01)
    if(money >= X):
        print(counter)
        exit()