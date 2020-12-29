S = input()

for s in S[::2]:
    if not s in ['R','U','D']:
        print("No")
        exit()
    
for s in S[1::2]:
    if not s in ['L','U','D']:
        print("No")
        exit()
print("Yes")
