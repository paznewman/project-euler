""" The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
"""

def prime_factors(n):
    if n%2 == 0:
        yield 2 
    while n%2 == 0:
        n /= 2
    i = 3
    while n >= i:
        if n%i == 0:
            yield i
            while n%i == 0:
                n /= i
        i += 2

print(max(prime_factors(600851475143)))
