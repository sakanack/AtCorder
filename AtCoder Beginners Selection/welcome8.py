N = int(input())
d = []
for i in range(N):
    d.append(int(input()))

unique_d = list(set(d))
print(len(unique_d))
