S = input()
T = input()

for i in reversed(range(len(T))):
    for j in range(len(T)-i):
        print(i+1, j)
        subStr = T[j:i+1+j]
        print(S, subStr)
        if(subStr in S):
            print("一致", len(T)-(i+1))
            print("find", S.find(subStr))
            print("rfind", S.rfind(subStr))
            print("位置i,j=",i,j)
            if(S.find(subStr) >= j):
                if(S.rfind(subStr)+len(T) <= len(S)):
                    print(len(T)-(i+1))
                    exit()
print(len(T))