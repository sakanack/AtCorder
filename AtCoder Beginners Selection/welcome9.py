N,Y = map(int, input().split(' '))

for x in range(N+1):
    y = (Y - (1000 * N) - (9000 * x)) / 4000
    z = ((5000 * N) - Y + (5000 * x)) / 4000
    if y.is_integer() and y >= 0 and z.is_integer() and z >= 0:
        print('{} {} {}'.format(x,int(y),int(z)))
        exit()
print('-1 -1 -1')