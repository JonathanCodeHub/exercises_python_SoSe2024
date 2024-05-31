# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:02:48 2024

@author: jonat
"""
import numpy as np
from numpy.linalg import inv

M= np.array([[3,1],[2,4]])
M_inv= inv(M)


print (M_inv)
print (M)