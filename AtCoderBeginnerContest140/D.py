N,K = map(int,input().split())

S = input()

def happy_count(s):
    print("happy",s)
    happy = 0
    for i in range(len(s)):
        if s[i] == "L":
            if i == 0:
                continue
            if s[i-1] == "L":
                happy += 1
        if s[i] == "R":
            if i == N-1:
                continue
            if s[i+1] == "R":
                happy += 1
    return happy

def rotate_point(str):
    lL = str.find("L")
    rL = str.rfind("L")
    lR = str.find("R")
    rR = str.rfind("R")
    L_len = rL - lL
    R_len = rR - lR
    if L_len > R_len:
        return (lL+1,rL-1)
    else:
        return (lR+1,rR-1)

def rotation(s,lp,rp):
    bstr = s[lp:rp+1]
    bstr = bstr[::-1]
    bstr = bstr.translate(str.maketrans({"L":"R","R":"L"}))
    return s[:lp]+bstr+s[rp+1:]

p = rotate_point(S)

print(rotation(S,p[0],p[1]))
ans_str = S
for i in range(K):
    p = rotate_point(S)
    ans_str = rotation(ans_str,p[0],p[1])
    print("ams",ans_str)
    print(happy_count(ans_str))