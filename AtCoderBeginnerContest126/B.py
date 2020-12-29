S = input()

head = int(S[0:2])
tail = int(S[2:4])

if head >= 1 and head <= 12:
    if tail >= 1 and tail <= 12:
        print('AMBIGUOUS')
    elif tail <=99:
        print('MMYY')
elif head <= 99:
    if tail >= 1 and tail <= 12:
        print('YYMM')
    elif tail <= 99:
        print('NA')