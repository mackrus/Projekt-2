import numpy as np
import random as r

n = 1


def rand_gen(n):
    return r.randint(0, n) ** n * np.pi


print(rand_gen(n))
