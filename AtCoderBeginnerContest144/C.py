N = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

divisors = make_divisors(N)
length = len(divisors)
if length % 2 == 1:
    ans = (divisors[length // 2] * 2) - 2
    print(ans)
    exit()

if length % 2 == 0:
    ans = divisors[(length // 2)-1] + divisors[length // 2] - 2
    print(ans)
    exit()