N = int(input())
A = list(map(int, input().split()))

def reciprocal(n):
    return 1 / n

rec_A = list(map(reciprocal, A))

print(1 / sum(rec_A))