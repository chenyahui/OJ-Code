# https://www.codewars.com/kata/playing-with-digits/
import math
def dig_pow(n, p):
    s = str(n)
    sum = 0
    for a in s:
        sum += math.pow(int(a), p)
        p += 1
    return sum / n if sum % n == 0 else -1 