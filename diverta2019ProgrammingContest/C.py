N = int(input())

S = []
for i in range (N):
    S.append(input())

ab_count = 0
bottom_a = 0
top_b = 0
ba = 0
for s in S:
    if s[-1] == 'A' and s[0] == 'B':
        ba += 1
    else:
        if s[-1] == 'A':
            bottom_a += 1
        if s[0] == 'B':
            top_b += 1
    for i in range(1,len(s)):
        if s[i-1] == 'A' and s[i] == 'B':
            ab_count += 1
if ba > 0:
    if bottom_a > 0:
        bottom_a -= 1
        ab_count += 1
    if top_b > 0:
        top_b -=  1
        ab_count += 1
ans = max(ba - 1, 0) + min(bottom_a, top_b) + ab_count
print(ans)