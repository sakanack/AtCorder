N,K=map(int,input().split())
S=input()
First=S[0]
Now=First
cnt=0
A=[0]
for s in S:
    if Now=='1' and s=='0':
        A+=[cnt]
        Now='0'
    elif Now=='0' and s=='1':
        A+=[cnt]
        Now='1'
    cnt+=1
A+=[N]
dp=2*K+1
ans=[]

if First=="0":
    p=1
    ans.append(A[min(dp-1,len(A)-1)])
else:
    p=0
    ans.append(A[min(dp,len(A)-1)])

while p+dp<len(A):
	ans.append(A[p+dp]-A[p])
	p+=2
ans.append(N-A[p])
#print(A)
print(max(ans))
