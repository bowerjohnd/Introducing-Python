# 22- interpreter work, math

import math

# pi and e
print('=' * 50, 'pi and e')
print(math.pi)
print(math.e)

# fabs
print('=' * 50, 'fabs()')
print(math.fabs(98.6))
print(math.fabs(-271.1))

# floor and ceil
print('=' * 50, 'floor() and ceil()')
print(math.floor(98.6))
print(math.floor(-271.1))
print(math.ceil(98.6))
print(math.ceil(-271.1))

# factorial
print('=' * 50, 'factorial()')
print(math.factorial(0))
print(math.factorial(1))
print(math.factorial(2))
print(math.factorial(3))
print(math.factorial(10))

# log
print('=' * 50, 'log()')
print(math.log(1.0))
print(math.log(math.e))
# log with different base
print(math.log(8, 2))

# pow
print('=' * 50, 'pow()')
print(math.pow(2,3))
print(2**3)
print(2.0**3)

# sqrt
print('=' * 50, 'sqrt()')
print(math.sqrt(100.0))
#print(math.sqrt(-100.0))

# trigonometry: sin, cos, tan, asin, acos, atan, atan2, hypot
print('=' * 50, 'trigonometry: sin(), cos(), tan(), etc.')
x = 3.0
y = 4.0
print('pythagorean theorem x=3 y=4 hypot()=', math.hypot(x, y))
print(math.sqrt(x*x + y*y))
print(math.sqrt(x**2 + y**2))

# radians and degrees
print('=' * 50, 'radians(), degrees()')
print(math.radians(180.0))
print(math.degrees(math.pi))
