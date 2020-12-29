
a = input()
b = input()
c = input()
x = input()

A = int(a)
B = int(b)
C = int(c)
X = int(x)

AA,BB,CC = 30,40,50
def pay_pattern(yen, ca, cb, cc, mode = 3):
    if yen == 0:
        return 1
        
    x = 0
    if mode == 3 and yen >= 500 and ca > 0:
        x = x + pay_pattern(yen-500, ca-1, cb, cc, 3)
    if mode >= 2 and yen >= 100 and cb > 0:
        x = x + pay_pattern(yen-100, ca, cb-1, cc, 2)
    if mode >= 1 and yen % 50 == 0 and (yen / 50) <= cc:
        x = x + pay_pattern(yen%50, ca, cb, cc - yen/50, 1)
    return x

x1 = pay_pattern(X,A,B,C)
print(x1)