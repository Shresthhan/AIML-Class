import numpy as np 
'''
arr = np.array([[1, 2, 3, 4, 5] , 
                [6, 7, 8, 9, 0]])

print(arr[0: , 1:3])
'''

# Copy VS View 
'''
np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np2 = np1.view()

print(f"Original np1 = {np1}")
print(f"Original np2 = {np2}")

np1[0] = 10
print(f"Changed np1 = {np1}")   # -> Whenever we change the original, the view changes too and vise versa i.e. both are connected
print(f"Changed np2 = {np2}")


np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np2 = np1.copy()

print(f"Original np1 = {np1}")
print(f"Original np2 = {np2}") 

np1[0] = 10
print(f"Changed np1 = {np1}")
print(f"Changed np2 = {np2}")
'''


