X, Y = map(int, input().split())

B = (Y / 2) - X
A = X - B

if(not B.is_integer()):
    print("No")
    exit()
if(B < 0):
    print("No")
    exit()
if(A < 0):
    print("No")
    exit()

print("Yes")