# 22-2 complex numbers, decimals, fractions

# complex numbers: real and imaginary
print('=' * 50)
print('a real number:', 5)
print('an imaginary number:', 8j)
print('an imaginary number:', 3 + 2j)
print(1j * 1j)
print((7+1j) * 1j)

# decimals
print('=' * 50)
x = 10.0 / 3.0
print(x)

print('=' * 50)
from decimal import Decimal
price = Decimal('19.99')
tax = Decimal('0.06')
total = price + (price * tax)
print(total)
penny = Decimal('0.01')
print(total.quantize(penny))    #quantize

# fractions
print('=' * 50)
from fractions import Fraction
print('1/3 * 2/3 =', Fraction(1, 3) * Fraction(2, 3))
print(Fraction(1.0/3.0))
print(Fraction(Decimal('1.0')/Decimal('3.0')))

# fractions.gcd() is now deprecated, use math.gcd()
#import fractions
#print('Greatest Common Denominator 24/16:', fractions.gcd(24, 16))
import math
print('Greatest Common Denominator 24/16:', math.gcd(24, 16))
