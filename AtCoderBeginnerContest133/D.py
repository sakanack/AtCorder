N = int(input())

A = list(map(int,input().split()))

ans = [0] * N

for i in range(N):
    if i == 0:
        il = N-1
    else:
        il = i-1
    if i == N-1:
        ir = 0
    else:
        ir = i+1
    
    while(A[i] != 0):
        print(A)
        if A[il] == 0 and A[ir] == 0:
            break
        
        if A[il] <= A[ir]:
            buf = min(A[i],A[ir])
            ans[ir] = ans[ir] + buf * 2
            A[i] = A[i] - buf
            A[ir] = A[ir] - buf
            print("R",i,buf,A[i],A[ir])
            print(A,ans)

        if A[il] > A[ir]:
            buf = min(A[il],A[i])
            ans[i] = ans[i] + buf * 2
            A[i] = A[i] - buf
            A[il] = A[il] - buf
            print("L",i,buf,A[i],A[ir])
            print(A,ans)

print(ans)