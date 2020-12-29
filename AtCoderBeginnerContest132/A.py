S = input()
unique = set(S)

if len(unique) != 2:
    print("No")
    exit()

for u in unique:
    if S.count(u) != 2:
        print("No")
        exit()
    
print("Yes")