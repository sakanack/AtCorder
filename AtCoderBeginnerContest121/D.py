A,B = map(int,input().split())

Aodd = -1
Beven = -1
if A % 2 == 1:
    Aodd = A
    A += 1
if B % 2 == 0:
    Beven = B
    B -= 1

ans = ((B-A) // 2 + 1) % 2
if Aodd != -1:
    ans = ans ^ Aodd
if Beven != -1:
    ans = ans ^ Beven

print(ans)