N = int(input())
S = input()

half_position = int(N/2)
l_str = S[0:half_position]
r_str = S[half_position:N]

if(l_str == r_str):
    print("Yes")
else:
    print("No")