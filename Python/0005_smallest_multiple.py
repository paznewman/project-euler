""" 2520 is the smallest number that can be divided by each of
    the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly
    divisible by all of the numbers from 1 to 20?
"""

# has to be divisble by all the primes smaller than 20 at least once.
# this leaves out the numbers 4,6,8,9,10,12,14,15,16,18,20
# 6, 10, and 14 are all a product of two and another prime, so they are already a divisor of the product of the primes
# 15 is 3*5 so we don't need it either
# we are left with 4, 8, 9, 12, 16, 20
# 4, 8 and 16 are powers of 2, so we can add 3 more 2's two the product for it to be divisible by 16 and tall the others
# 9 is 3*3 so we need to add another 3 to the product
# 12 is 3*4, but since we added the additional 2's, the product is already divisble by it
# same goes for 20: 2*2*5

print(2*2*2*2*3*3*5*7*11*13*17*19)
