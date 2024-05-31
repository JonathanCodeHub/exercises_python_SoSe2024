# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:17:18 2024

@author: jonat
"""

import numpy as np
from numpy.linalg import inv

A= np.array([
    [7,5,-3],
    [3,-5,2,],
    [5,3,-7]])
r=np.array([[16],
           [-8],
           [0]])
b=np.array(["x","y","z"])

A_inv= inv(A)

x=np.dot(A_inv,r)

print(x)
