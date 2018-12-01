""" By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.

    What is the 10001st prime number?
"""

primes_list = [2]
index = 1
n = 3
while (index < 10001):
    n_is_prime = True
    for p in primes_list:
        if n%p == 0:
            n_is_prime = False
            break
    if n_is_prime:
        primes_list.append(n)
        index += 1
    n += 2

print(primes_list[10000])
