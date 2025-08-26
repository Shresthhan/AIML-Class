'''  LINEAR TRANSFORMATION  '''

import numpy as np

# Scaling 
'''
kx , ky = 2 , 3
A = np.array([[kx , 0],
              [0 , ky]])
x = np.array([4 , 5])
Tx = A @ x

print(f"T(x) = {Tx}")
'''

# Rotation
'''
theta = np.pi /2 # 90 degrees
A = np.array([[np.cos(theta) , -np.sin(theta)],
              [np.sin(theta) , np.cos(theta)]])

x = np.array([3 , 2])  # Original Vector
rotated_vector = A @ x
print(f"Original Vector = {x}")
print(f"Rotated Vector = {rotated_vector}")
'''

# Reflection 
'''
A = np.array([[1 , 0],
              [0 , -1]]) # -> For reflection along X axis 
x = np.array([4 , 5])
reflected_vector = A @ x
print(f"Original Vector = {x}")
print(f"Reflected Vector = {reflected_vector}")
'''

#  Composition of Linear Transformations
A = np.array([[2, 3],
              [4, 9]])
B = np.array([[4, 7],
              [4, 10]])

x = np.array([1, 2])

result1 = B @ (A @ x)

intermediate_matrix = B @ A  # B @ (A @ x) = (B @ A) @ x 

result2 = intermediate_matrix @ x 

print(result1)
print(result2)