N,K = map(int, input().split(' '))
S = input()

s_len = len(S)

check_i = [0] + [i+1 for i in range(s_len-1) if S[i] != S[i+1]]

maxvalue = 0
mode = 0
for i in check_i:
    count = 0
    life = K
    for s in S[i:s_len]:
        if mode == 0 and s == '0':
            if life <= 0: break
            life -= 1
            mode = 1
        elif mode == 1 and s == '1':
            mode = 0
        count += 1
    if maxvalue < count:
        maxvalue = count
print(maxvalue)