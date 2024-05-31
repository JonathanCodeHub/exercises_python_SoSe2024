# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:43:27 2024

@author: jonat
"""

import numpy as np
from math import log10

x= np.array([[1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]] )

x_np= np.log10(x)

print(x_np)

#leeres Array für Ergebnisse
x_for = np.zeros_like(x)

for i in range(x.shape[0]):#i ist so lang wie das Array
    for j in range (x.shape[1]):
        x_for[i,j]= log10(x[i,j]) 

print(x_for[0])