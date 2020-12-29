A,B = map(int, input().split())

if A >= 13:
    print(B)

if A <= 12 and A >= 6:
    print(int(B/2))

if A <= 5:
    print(0)
