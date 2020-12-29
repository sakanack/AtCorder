S = input()

T_matcher = ['dream', 'dreamer', 'erase','eraser']

T = ''
while(True):
    flag = True
    for m in T_matcher:
        if S.endswith(m + T):
            T = m + T
            flag = False
    else:
        if flag: break

if S == T:
    print('YES')
else:
    print('NO')