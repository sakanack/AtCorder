import collections

N = int(input())

a = list(map(int, input().split()))

a_coll  = collections.Counter(a)
a_key   = list(a_coll.keys())
a_value = list(a_coll.values())

if N % 3 != 0:
    if len(a_key) == 1 and a_key[0] == 0:
        print("Yes")
        exit()
    else:
        print("No")
        exit()

if len(a_key) == 1:
    if a_key[0] == 0:
        print("Yes")
        exit()

if len(a_key) == 2:
    if 0 in a_key:
        for key, count in zip(a_key,a_value):
            if key == 0:
                if count != int(N/3):
                    print("No")
                    exit()
            else:
                if count != int(2*N/3):
                    print("No")
                    exit()
        print("Yes")
        exit()
        
if len(a_key) == 3:
    for count in a_value:
        if count != int(N / 3):
            print("No")
            exit()
        
    if a_key[0] ^ a_key[1] == a_key[2]:
        print("Yes")
        exit()

print("No")