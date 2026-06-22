"""
Ufunc
"""

import numpy as np

def myadd(x,y):
    return x+y

x = np.frompyfunc(myadd, 2, 1)
print(x([1, 2, 3, 4], [5, 6, 7, 8]))