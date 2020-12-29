N = int(input())

A = [int(input()) for _ in range(N)]

length = N
ans = 0
while A:
    ans += 1
    head = A[0]
    del A[0]
    length -= 1
    i = 0
    while i < length:
        #print(A,head,A[i])
        if head < A[i]:
            head = A[i]
            #print("del",A[i])
            del A[i]
            length -= 1
        else:
            i += 1

print(ans)