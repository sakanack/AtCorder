H = int(input())

d = {}
d = {1:1}
def f(n):
    if(d.get(n) != None):
        return d[n]
    buf = f(int(n/2)) + f(int(n/2)) + 1
    d[n] = buf
    return buf

print(f(H))