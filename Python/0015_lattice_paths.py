""" Starting in the top left corner of a 2×2 grid,
    and only being able to move to the right and down,
    there are exactly 6 routes to the bottom right corner.

    How many such routes are there through a 20×20 grid?
"""

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def choose(n, k):
    return factorial(n)//(factorial(k)*factorial(n-k))

print(choose(40,20))    
