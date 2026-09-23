################################################
# 22-4 numpy linear algebra
################################################

import numpy as np

print('=' * 50)
print('4x + 5y = 20')
print('x + 2y = 13')

coefficients = np.array([ [4,5], [1,2] ])   # left side multipliers to x and y
dependents = np.array( [20, 13] )           # right side of equation

answers = np.linalg.solve(coefficients, dependents)     # feels like cheating
print('x =', answers[0], '\ny =', answers[1])
print('do these answers solve it?')
print('4x + 5y =', ( (4 * answers[0]) + (5 * answers[1]) ))
print('x + 2y =', ( (answers[0]) + (2 * answers[1]) ))

product = np.dot(coefficients, answers)
print('dot product', product)

print('alllclose', np.allclose(product, dependents))