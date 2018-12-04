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

def partial_factorial(start, end):
    # start*(start+1)*(start+2)*...*(end-1)*end
    result = 1
    while end >= start:
        result *= end
        end -= 1
    return result


print(partial_factorial(20, 40)//(2*factorial(20)))
    
