import re

S = input()

pattern = '[A|C|G|T]+'
matchall = re.findall(pattern, S)

if matchall:
    print(max(map(len,matchall)))
else:
    print('0')