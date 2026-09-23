################################################
# 22-3 numpy arrays
################################################

import numpy as np

# numpy array
print('=' * 50)
b = np.array( [2, 4, 6, 8] )
print(b)
print('rank', b.ndim)
print('size', b.size)
print('shape', b.shape)

# numpy arange (a range?)
print('=' * 50)
a = np.arange(10)
print(a)
print(a.ndim)
print(a.size)
print(a.shape)

a = np.arange(7, 11) # from 7 to 10 (11 - 1)
print(a)
a = np.arange(7, 11, 2) # step size of 2
print(a)

f = np.arange(2.0, 9.8, 0.3)
print(f)

g = np.arange(10, 4, -1.5, dtype=float) # specify type to use
h = np.arange(10, 4, -1.5, dtype=int) # step gets rounded to -2
print(g, '\n', h)

# numpy array with zeros(), ones(), random()
print('=' * 50)
a = np.zeros((3,)) 
print(a)
print(a.ndim)
print(a.size)
print(a.shape)

b = np.zeros((2, 4))    # rank (dimensions) of 2 
print(b)
print(b.ndim)
print(b.size)
print(b.shape)

k = np.ones((3, 5))
print(k)
print(k.ndim)
print(k.size)
print(k.shape)

m = np.random.random((3,5)) # random between 0.0 and 1.0
print(m)
print(m.ndim)
print(m.size)
print(m.shape)

# change array shape with reshape()
print('=' * 50)

a = np.arange(10)
print('---------- \n',a)

a = a.reshape(2,5)
print('---------- \n',a)
print(a.ndim)
print(a.size)
print(a.shape)

a = a.reshape(5,2)
print('---------- \n',a)
print(a.ndim)
print(a.size)
print(a.shape)

a.shape = (2, 5)
print('---------- \n',a)
print(a.ndim)
print(a.size)
print(a.shape)
#a = a.reshape(3,4)  # error, must be same size as original

# numpy array get an element with []
a = np.arange(10)
print('----------')
print(a[7])
print(a[-1])

a.shape = (2, 5)
print('----------')
print(a)
print( a[1,2] )
print('----------')

l = [ [0,1,2,3,4], [5,6,7,8,9] ]    # regular two-dimensional list
print(l)
#print( l[1,2] )    # numpy way
print( l[1][2] )    # list way

# numpy array slices
print('----------')
a = np.arange(10)
a = a.reshape(2,5)
print(a)
print(a[0, 2:])     # first row 0, elements from offset (index) 2 to end
print(a[-1, :3])    # last row -1, elements from start to before index 3 (0 to 2)
a[:, 2:4] = 1000 # assign value 1000 to all rows, only to indexes 2 and 3
print(a)

# numpy array math
print('----------')
a = np.arange(4)
print(a)
a *= 3                          # math directly on numpy array
print(a)
print('----------')

plain_list = list(range(4))
print(plain_list)
plain_list = [num * 3 for num in plain_list]    # normal list requires loop
print(plain_list)

print('----------')

a = np.zeros( (2, 5) ) + 17.0          # initialize all elements with 0 + 17.0
print(a)
