N, A, B, C, D = map(int, input().split())
S = input()

if C < D:
    for i in range(A-1,D-1):
        if S[i] == '#' and S[i+1] =='#':
            print('No')
            exit()
    print('Yes')

if C > D:
    for i in range(A-1,C-1):
        if S[i] == '#' and S[i+1] =='#':
            print('No')
            exit()
    for i in range(B-2,D-2):
        if S[i] == '.' and S[i+1] == '.' and S[i+2] == '.':
            print('Yes')
            exit()
    print('No')