N = int(input())

for i in range(1,10):
    check = N / i
    if check.is_integer() and check < 10:
        print("Yes")
        exit()

print("No")