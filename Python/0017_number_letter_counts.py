""" If the numbers 1 to 5 are written out in words:
        one, two, three, four, five,
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were
    written out in words, how many letters would be used?
"""

def num_to_words(num):
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "xeventy", "eighty", "ninety"]

    if num < 1:
        return ""
    if num < 10:
        return digits[num-1]
    if num < 20:
        return teens[num%10]
    if num < 100:
        return tens[num//10 - 2] + num_to_words(num%10)
    if num < 1000:
        if num % 100 == 0:
            return digits[num//100 - 1] + "hundred"
        else:
            return digits[num//100 - 1] + "hundred" + "and" + num_to_words(num%100)

letter_count = 0
for i in range(1,1000):
    letter_count += len(num_to_words(i))
print(letter_count + len("onethousand"))

