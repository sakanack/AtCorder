K = int(input())


count = 0
def counter(atai, keta, runrun=0):
    global count
    # print(atai, keta)
    runrun = runrun + atai*(10**(keta-1))
    if (keta==1):
        count += 1
        print(count)
        print(runrun)
        return 1

        # if(atai != 0 or atai!=9):
        #     return 3
        # return 2
    if(atai==0):
        return counter(atai, keta-1, runrun) + counter(atai+1, keta-1, runrun)
    elif(atai==9):
        return counter(atai-1,keta-1, runrun) + counter(atai,keta-1, runrun)
    else:
       return counter(atai-1,keta-1, runrun) + counter(atai,keta-1, runrun) + counter(atai+1,keta-1, runrun)

counter(8,100)

# count = 0
# for j in range(100):
#     for i in range(1,10):
#         count += counter(j,i)
#         # print(count)