""" A palindromic number reads the same both ways. The largest palindrome
    made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n):
    s = str(n)
    s1 = s[:int(len(s)/2)]
    s2 = s[len(s1):]
    return s1 == s2[::-1]


biggest = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        t = i*j
        if is_palindrome(t) and t > biggest:
            biggest = t

print(biggest)
