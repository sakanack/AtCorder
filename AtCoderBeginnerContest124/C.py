S = input()

le = len(S)
w_pattern = '10'
b_pattern = '01'

A = (w_pattern * int(le/2 + 1))[0:le]
B = (b_pattern * int(le/2 + 1))[0:le]

w_ans = sum([s != a for s,a in zip(S,A)])
b_ans = sum([s != b for s,b in zip(S,B)])
ans = w_ans if w_ans < b_ans else b_ans

print(ans)