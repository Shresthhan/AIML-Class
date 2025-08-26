import numpy as np

A = np.array([[1,0,1],
              [0,1,1],
              [0,1,1]])

print("Rank:", np.linalg.matrix_rank(A))

basis = []
B = []

for i in range(A.shape[1]):
    test = B + [A[:,i]]
    if np.linalg.matrix_rank(np.column_stack(test)) > len(B):
        B.append(A[:,i])
        basis.append(i+1)  

print("Basis columns are:", basis)
