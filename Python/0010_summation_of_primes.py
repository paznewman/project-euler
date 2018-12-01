""" The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
"""

def primes(n):
    """ generates all prime numbers smaller than _n_
        using the Sieve of Eratosthenes
    """
    sieve = [True]*n
    for p in range(2, n):
        if sieve[p]:
            yield p
            for i in range(p*p, n, p):
                sieve[i] = False

print(sum(primes(2000000)))
