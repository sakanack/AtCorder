A,B = map(int, input().split(' '))

count = 0
for i in range(2):
    if A <= B:
        count += B
        B -= 1
    else:
        count += A
        A -= 1
print(count)