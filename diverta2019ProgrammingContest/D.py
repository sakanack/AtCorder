N = int(input())

divisors = []
for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        divisors.append(i)
        if i != N // i:
            divisors.append(N//i)

m_list = []
for k in divisors:
    if N % k == 0 and N > k:
        m = int((N / k) - 1)
        if k == N%m:
            A = N / (m + 1)
            m_list.append(m)

print(sum(m_list))