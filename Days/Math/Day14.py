# Broadcasting 

import numpy as np

# Scaler to vector broadcasting
'''
arr = np.array([1, 2, 3, 4, 5])
s = 5 
new_arr = arr * s
print(arr)
print(new_arr)
'''

# S -> M 
'''
s = 4
mat = np.array([[1, 2, 3],
                [3, 4, 5],
                [6, 7, 8]])
new_mat = mat * s
print(new_mat)
'''

# V -> M
'''
arr = np.array([1, 2, 3])
mat = np.array([[1, 2, 3],
                [3, 4, 5],
                [6, 7, 8]])
new_mat = mat + arr
print(mat)
print(new_mat)
'''

# Sorting 
'''
a = np.array([5, 8, 2, 9, 3])
print(np.sort(a)) # Ascending
print(np.sort(a)[::-1]) # Descending
'''
'''
a = np.array([[4, 3, 7],
              [6, 3, 4],
              [7, 9, 6]])
print(np.sort(a , axis = 1))   # NOTE -> Row lai sort garna column ko value herna parcha so axis = 1
print(np.sort(a , axis = 0))    # Similarly column sort garna row ko value herchau
'''

# Append row
'''
m = np.array([[4, 3, 7],
              [6, 3, 4]])

a1 = np.array([[7, 9, 6]])

a2 = np.array([[3, 2, 8]])

new1 = np.append(m, a1, axis = 0)
new2 = np.append(new1, a2, axis = 0)
print(m)
print()
print(new1)
print()
print(new2)
'''

# Append column 
m = np.array([[4, 3, 7],
              [6, 3, 4]])

a = np.array([[1],
              [2]])
new = np.append(m, a, axis = 1)
print(new)