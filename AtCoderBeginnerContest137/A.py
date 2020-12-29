A,B = map(int,input().split())

plus =  A + B
minus = A - B
mult =  A * B

a_list = []
a_list.append(plus)
a_list.append(minus)
a_list.append(mult)

print(max(a_list))