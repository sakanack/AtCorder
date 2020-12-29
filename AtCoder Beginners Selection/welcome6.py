N, A, B = map(int, input().split())

count = 0
for i in range(N+1):
    sums = sum(map(int,str(i)))
    if A <= sums and sums <= B:
        count = count + i 
print(count)
