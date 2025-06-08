import numpy as np

A = np.array([[4, 0], [0, -4]])

eigs = np.linalg.eig(A)


print(eigs)
