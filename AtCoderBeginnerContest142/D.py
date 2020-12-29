def prime_factorize(n):
    a = []
    a.append(1)
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

A, B = map(int, input().split())
a_prime = set(prime_factorize(A))
b_prime = set(prime_factorize(B))
prime = a_prime & b_prime
print(len(prime))
