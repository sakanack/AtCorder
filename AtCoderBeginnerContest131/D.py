N = int(input())

job = [ list(map(int,input().split())) for _ in range(N)]
job.sort(key=lambda x:x[1])

time = 0
for t, deadline in job:
    time += t
    if time > deadline:
        print("No")
        exit()
print("Yes")