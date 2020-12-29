S = input()

length =  len(S)

if (length == 1):
    print('0')
    exit()

if ((length % 2) == 1):
    rev = S[(length//2 + 1):][::-1]
    count = 0
    for i in range(len(rev)):
        if (S[i] != rev[i]):
            count += 1

if ((length % 2) == 0):
    rev = S[(length//2):][::-1]
    count = 0
    for i in range(len(rev)):
        if (S[i] != rev[i]):
            count += 1
print(count)