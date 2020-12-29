r ,D , x2000 = map(int, input().split())

xi = x2000
for i in range(1,11):
    xi = r * xi - D
    print(xi)