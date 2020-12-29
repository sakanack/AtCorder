import math
import itertools

N = int(input())
positons = [list(map(int, input().split())) for _ in range(N)]

def euclid(pos1, pos2):
    return math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)

def dist(posList):
    ans = 0
    for i in range(1,len(posList)):
        ans += euclid(posList[i-1], posList[i])
    return ans

sumdist = 0
for conb in itertools.permutations(positons, len(positons)):
    sumdist += dist(conb)

ans = sumdist / math.factorial(len(positons))
print(ans)
