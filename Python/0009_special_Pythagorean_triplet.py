""" A Pythagorean triplet is a set of three natural numbers, a < b < c,
    for which a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
"""

def sum_triplets (n):
    """ generates all triplets of natural numbers which sum up to _n_. """

    def sum_pairs (n):
        """ generates all pairs of natural numbers which sum up to _n_. """
        a = n-1
        while a >= 1:
            yield [a, n-a]
            a-=1
            
    a = n-2
    while a >= 2:
        for pair in sum_pairs(n-a):
            yield [a] + pair
        a-=1


for triplet in sum_triplets(1000):
    c = triplet[0]  # we know c has to be bigger than a and b
    a = triplet[1]
    b = triplet[2]
    if a*a + b*b == c*c:
        print(a*b*c)
        break
