# 분수의 덧셈 - retry
import math
def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    gcd = math.gcd(denom, numer)
    return [numer//gcd, denom//gcd]

# Best solution
from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    answer = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    return [answer.numerator, answer.denominator]