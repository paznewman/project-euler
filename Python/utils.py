
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def digit_sum(n):
    result = 0
    while n > 0:
        result += n%10
        n //= 10
    return result
