A,B = map(int, input().split())

AB = (A + B) / 2

if AB.is_integer():
    print(int(AB))
else:
    print("IMPOSSIBLE")