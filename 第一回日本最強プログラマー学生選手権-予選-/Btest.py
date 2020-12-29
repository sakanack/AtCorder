def souwa(num):
    if num % 2 == 0:
        return int((num+1) * (num/2))
    else:
        return int((num+1) * (num//2)) + ((num//2)+1)
 
for i in range(10**8,10**9):
    if souwa(i-1) == i*(i-1)//2:
        # print("OK")
        # print(souwa(i-1), i*(i-1)//2)

    else:
        print(souwa(i), i*(i-1)//2)
        print("warn")