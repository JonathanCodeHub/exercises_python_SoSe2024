# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:16:41 2024

@author: jonat
"""

import matplotlib.pyplot as plt

a=1
r=0.5
n=10
s_n=[]
summe =0

for k in range (0,n):
   summe += a * r ** k
   s_n.append(summe)
   
print(s_n)

plt.plot(s_n)
