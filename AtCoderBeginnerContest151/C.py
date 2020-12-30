N, M = map(int, input().split())
submitList = [tuple(input().split()) for _ in range(M)]

completeList = [0] * (N+1)
WAcountList = [0] * (N+1)
ACcount = 0
WAcount = 0

for i in range(M):
    question = int(submitList[i][0])
    result = submitList[i][1]
    if(completeList[question] == 1):
        continue
    if(result == "AC"):
        completeList[question] = 1
        ACcount += 1
        WAcount += WAcountList[question]
        continue
    if(result == "WA"):
        WAcountList[question] += 1
    
print(ACcount, WAcount)