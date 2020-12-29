a = input()
b,c = input().split(' ')
s =  input()


def sum_print(a,b,c,s):
    x = int(a) + int(b) + int(c)
    print('{} {}'.format(x,s))

sum_print(a,b,c,s)